import streamlit as st 
from langchain import PromptTemplate, LLMChain
from langchain.llms import GPT4All
from docxtpl import DocxTemplate
import io

# Model Logic
@st.cache_resource
# Model path
def load_model():
    path = r"D:\Great learning\NLP\LLM models\wizardlm-13b-v1.1-superhot-8k.ggmlv3.q4_0.bin"
    # model call
    llm = GPT4All(model=path,verbose=True)
    return llm
llm = load_model()

context = {}

# Web UI Tabs
per_info,career_info,projects,education_info,skills = st.tabs(['personal_info','career_details','projects','education_info','skills'])
# Personal information UI
with per_info:
    st.header("Enter your personal information")
    col_1,col_2 = st.columns(2)
    with col_1:
        context['name'] = st.text_input('Name')
        st.subheader("Hobbies")
        context['interest_i'] = st.text_input("Hobby 1:")
        context['interest_ii'] = st.text_input("Hobby_2")
        context['interest_iii'] = st.text_input("Hobby_3")

    with col_2:
        context['phone_numer'] = st.text_input('Phone Number')
        context['email'] = st.text_input("Email address")
        context['git_hub'] = st.text_input("GitHub link")
        context['linkdin'] = st.text_input("Linkdin link")

    st.write("Continue to next page once all details are filled")

# Career information UI
with career_info:
    st.header("Enter your career details")

    summary = st.text_area('Career Summary',
                        value='Enter the details about your role or job description')
    
    prompt = PromptTemplate(input_variables=['action'], template="""
            ### Instruction:
            The prompt below is a question to answer, or write a professional career summary for the below prompt in 2 or 3 sentences ; decide which and write an appropriate response.
            ### Prompt: 
            {action}
            ### Response:""")
    llmchain = LLMChain(prompt=prompt,llm=llm,verbose = True)

    if st.button('Generate Career Summary'):
        context['summary'] = llmchain.run(summary)
        st.write(context['summary'])

    job_role,company,tenure = st.columns(3)

    with job_role:
        context['job_role_i'] = st.text_input("Job Title")
    with company:
        context['company_name_i'] = st.text_input("Company")
    with tenure:
        context['tenure_i'] = st.text_input("Tenure")

    work_exp = st.text_area('Work Experience',
                            value="Enter details about your work experience(2 or 3 valuable responsibilities)")
    prompt = PromptTemplate(input_variables=['action'], template="""
            ### Instruction:
            The prompt below is a question to answer, or write a professional career summary for the below prompt in 2 or 3 sentences ; decide which and write an appropriate response.
            ### Prompt: 
            {action}
            ### Response:""")
    llmchain = LLMChain(prompt=prompt,llm=llm,verbose = True)

    if st.button('Generate Work Experiance Summary'):
        context['work_exp_i'] = llmchain.run(work_exp)
        st.write(context['work_exp_i'])

    context['achievements_i'] = st.text_area('Achievement 1',value="Enter your achievements at previous job")
    context['achievements_ii'] = st.text_area('Achievement 2',value="Enter your achievements at previous job")
    
    st.write("Continue to next once all details are filled")

#Project details
with projects:
    st.header("Enter your Project details")

    prj_1 = st.text_area('Project 1',
                        value='Give some details about your project to generate')
    
    prompt = PromptTemplate(input_variables=['action'], template="""
            ### Instruction:
            The prompt below is a question to answer, or write a professional career summary for the below prompt in 2 or 3 sentences ; decide which and write an appropriate response.
            ### Prompt: 
            {action}
            ### Response:""")
    llmchain = LLMChain(prompt=prompt,llm=llm,verbose = True)

    if st.button('Generate Project Description'):
        context['projects'] = llmchain.run(prj_1)
        st.write(context['projects'])  ## -- need to  update the LLM result 

    prj_2 = st.text_area('Project 2',
                        value='Give some details about your project to generate')
    if st.button('Generate Project 2 Description'):
        context['project_ii'] = llmchain.run(prj_2)
        st.write(context['project_ii'])  ## -- need to  update the LLM result 

    st.write("Continue to next once all details are filled")

# Education info

with education_info:
    st.header("Enter your Education Details")
    course,institution,score,year = st.columns(4)
    with course:
        context['education_i'] = st.text_input("Qualificationn 1")
        context['education_ii'] = st.text_input("Qualificationn 2")
        context['education_iii'] = st.text_input("Qualificationn 3")
    with institution:
        context['college_i'] = st.text_input("university 1")
        context['college_ii'] = st.text_input("university 2")
        context['college_iii'] = st.text_input("university 3")
    with score:
        context['grade_i'] = st.text_input("Score/CGPA 1")
        context['grade_ii'] = st.text_input("Score/CGPA 2")
        context['grade_iii'] = st.text_input("Score/CGPA 3")
    with year:
        context['year_i'] = st.text_input("Year of completion 1")
        context['year_ii'] = st.text_input("Year of completion 2")
        context['year_iii'] = st.text_input("Year of completion 3")
    
    st.write("Continue to next once all details are filled")

# Skills

with skills:
    st.header("Enter Your Key Skills")
    skill , certificates = st.columns(2)
    with skill:
        context['skill_i'] = st.text_input('Skill 1')
        context['skill_ii'] = st.text_input('Skill 2')
        context['skill_iii'] = st.text_input('Skill 3')
        context['skill_iiii'] = st.text_input('Skill 4')
    with certificates:
        certificate = st.text_area('Other certifications' , value="""1. certification 1
2.Certification 2
3. Certification 3""")
        
doc = DocxTemplate("GL+Resume+Template29.docx")

if len(context.keys()) == 34:
    if st.button("Generate Resume"):
        doc.render(context=context)
        doc_io = io.BytesIO()
        doc.save(doc_io)
        doc_io.seek(0)
        st.download_button("Download Resume",doc_io,file_name="Generated resume.docx",key="Download button")




# """
#             ### Instruction: 
#             The prompt below is a question to answer, a task to complete, or a conversation to respond to; decide which and write an appropriate response.
#             ### Prompt: 
#             {action}
#             ### Response:"""


