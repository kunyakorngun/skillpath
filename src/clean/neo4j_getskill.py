from neo4j import GraphDatabase
from clean.neo4j_skillpath import Neo4jSkillPath
from dotenv import load_dotenv
import os

load_dotenv()

# driver = Neo4jSkillPath("neo4j://neo4j:7687", "neo4j", os.getenv("NEO4J_PASSWORD"), os.getenv("NEO4J_DB_NAME"))

# # from src.clean.neo4j_skillpath import Neo4jSkillPath
# # from dotenv import load_dotenv
# # import os

# # load_dotenv()

# # # ✅ ใช้ localhost ถ้ารัน Neo4j ในเครื่อง


def get_skills_for_user_job_company(driver, user_name, job_name, company_name):
    query = """
    MATCH (u:User {name: $user_name})-[:HAS_SKILL]->(s:Skill)<-[:REQUIRE_SKILL]-(j:Job {name: $job_name})<-[:HAS_JOB]-(c:Company {name: $company_name})
    RETURN s.name AS skill_name
    """
    results = driver.run_query(query, {
        "user_name": user_name,
        "job_name": job_name,
        "company_name": company_name
    })
    return [record["skill_name"] for record in results]

# =======================
# ดึง skill สำหรับทุก job/company ที่ต้องการ
# =======================
def load_skill_dict(driver):
    user = "John"
    companies = ["SCG", "PTT"]
    jobs = [
        "Data Scientist",
        "Data Engineer",
        "Machine Learning Engineer",
        "Data Analyst",
        "Business Analyst"
    ]

    skill_dict = {}
    for company in companies:
        for job in jobs:
            skills = get_skills_for_user_job_company(driver=driver, user_name=user, job_name=job, company_name=company)
            key = f"skill_{company.lower()}_{job.lower().replace(' ', '')}"
            skill_dict[key] = skills
    print(skill_dict)
    return skill_dict

# if __name__ == "__main__": 
#     driver = Neo4jSkillPath("neo4j://neo4j:7687", "neo4j", os.getenv("NEO4J_PASSWORD"), os.getenv("NEO4J_DB_NAME"))
#     load_skill_dict(driver=driver)