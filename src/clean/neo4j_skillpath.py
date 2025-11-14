from neo4j import GraphDatabase
from dotenv import load_dotenv
import os

load_dotenv()

class Neo4jSkillPath:
    def __init__(self, uri, user, password, database):
        self.driver = GraphDatabase.driver(uri, auth=(user, password), database=database)
        try:
            self.driver.verify_connectivity() 
            print("connect successfully")
        except Exception as e:
            print(f"Error connecting to Neo4j: {e}")
        self.db = self.driver.session(database=database)
        
    def close(self):
        if self.db:
            self.db.close()
            print("Database connection closed.")
    
    def create_node_company(self, company, job, skill):
        query ="""
        MERGE (c:Company {name: $company})
        MERGE (j:Job {name: $job})
        MERGE (s:Skill {name: $skill})
        MERGE (c)-[:HAS_JOB]->(j) 
        MERGE (j)-[:REQUIRE_SKILL]->(s) 
        """
        self.db.run(
            query,  
            skill=skill,
            company=company,
            job=job)
        print("👍Node company created successfully.")
    
    def create_node_user(self, user, skill):
        query ="""
        MERGE (u:User {name: $user})
        MERGE (s:Skill {name: $skill})
        MERGE (u)-[:HAS_SKILL]->(s)
        """
        self.db.run(
            query,  
            user=user,
            skill=skill,
            )
        print("👍Node user created successfully.")
        
    def match_skill_node(self, user, skill, company, job):
        query ="""
        MATCH (u:User {name: $user})-[:HAS_SKILL]->(s:Skill {name: $skill})<-[:REQUIRE_SKILL]-(j:Job {name: $job})<-[:HAS_JOB]-(c:Company {name: $company})
        RETURN s.name AS skill_name
        """
        self.db.run(
            query,  
            user=user,
            skill=skill,
            company=company,
            job=job
            )
        print("👍Node user created successfully.")
        
    def run_query(self, query, parameters=None):
        """
        ใช้สำหรับ query ข้อมูลทั่วไป เช่น MATCH / RETURN
        """
        try:
            result = self.db.run(query, parameters or {})
            return [record for record in result]
        except Exception as e:
            print(f"❌ Query failed: {e}")
            return []
        
if __name__ == "__main__": 
        
    # neo4jskillpath = Neo4jSkillPath("bolt://localhost:7687", "neo4j", os.getenv("NEO4J_PASSWORD"), os.getenv("NEO4J_DB_NAME"))
    neo4jskillpath = Neo4jSkillPath("neo4j://neo4j:7687", "neo4j", os.getenv("NEO4J_PASSWORD"), os.getenv("NEO4J_DB_NAME"))
        
    data_company= {
        "SCG": {
            "jobs": {
                "Data Scientist": ["Python", "Machine Learning", "SQL", "Statistics", "Visualization"],
                "Data Engineer": ["Python", "ETL", "SQL", "Docker"],
                "Business Analyst": ["Excel", "SQL", "Visualization"]
            }
        },
        "PTT": {
            "jobs": {
                "Data Analyst": ["Python", "Power BI", "SQL", "Visualization"],
                "Machine Learning Engineer": ["Python", "TensorFlow", "MLOps", "Docker", "Data Preprocessing"]
            }
        }
    }

    data_user= {
        "John": ["Python", "Machine Learning", "SQL", "Statistics", "Visualization", "ETL", "Docker", "MLOps", "figma"]
    }

    for key, value in data_company.items():
        for job in value["jobs"]:
            for skill in value["jobs"][job]:
                neo4jskillpath.create_node_company(company=key, job=job, skill=skill)

    for key, value in data_user.items():
        for skill in value:
            neo4jskillpath.create_node_user(user=key, skill=skill)
            
        
    neo4jskillpath.close()

