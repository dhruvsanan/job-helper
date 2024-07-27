from st_copy_to_clipboard import st_copy_to_clipboard
import google.generativeai as genai
import streamlit as st
import os
# genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
genai.configure(api_key=os.getenv("GOOGLE_API _KEY"))


def get_gemini_response(a, b, c, d):
    model = genai.GenerativeModel('gemini-1.5-pro-latest')
    try:
        response = model.generate_content([a, b, c, d])
        return response.text
    except Exception as e:
        st.error(
            "Internal server error. Please check your internet connection and try again.")
        raise e


st.set_page_config(page_title="My Resume")

jt = ""
jd = ""
pdf_content = """Dhruv Sanan Education Indian Institute of Technology Madras Bachelor of Science (BS) in Data Science and Applications. CGPA 7.89 
    I.K.G Punjab Technical University Bachelor of Technology [B.Tech] in Computer Science and Engineering CGPA 7.72 
    Experience Nvision Soft (remote) Miami, Florida Jan 2024 – Mar 2024 ● Generative AI Full stack developer o Reduced hiring time by 60% by developing a smart Applicant Tracking System (ATS) and saving 20% in recruitment costs.
    o Automated resume review, enabling the processing of over 150 resumes per hour. o Applied advanced relevance techniques to shortlist the top 10% of candidates, ensuring high-quality hires and improved talent acquisition outcomes through cross-functional teamwork. 
    Indian Institute of Technology Madras (remote) Chennai, India ● Project Mentor/TA for Application Development Project (BSCS2003P) Aug 2023 – Dec 2023 o Mentored 20+ students in a comprehensive web application development project, resulting in 15+ fully functional web apps. o Delivered 40+ hours of instruction on HTML, CSS, JavaScript, Flask, and SQLite, enhancing students full-stack development capabilities. o Oversaw the implementation of secure authentication protocols and the integration APIs, improving app functionality and user experience. 
    ● Viva Examiner for Application Development Project (BSCS2006P) Aug 2023 – Dec 2023 o Conducted viva sessions for students, evaluating 100+ projects on advanced web technologies. o Provided constructive feedback, resulting in a 20% improvement in project quality and results. 
    Skills Artificial Intelligence: Langchain, LangGraph, Hugging Face, Crew AI, Open AI Assistant, Open Source LLMs, OpenAI, Google Gemini, Vector Databases, RAG Apps Frontend: React.js, Next.js, TypeScript, Tailwind, Shadcn, Vuejs Backend: Rest APIs, Node.js, Python, Stripe, Payload, Nodemailer, tRPC, Clerk, Flask, Resend, Redis, Celery, OpenCV Database: MySQL, Postgres, MongoDB, PineconeDB 
    Projects AI Lead Magnet - SaaS Product ● Developed a full-stack AI application that transforms standard content into interactive AI lead magnets, enhancing user engagement and lead generation. ● Engineered a dynamic front-end using Next.js, Tailwind CSS, and TypeScript, coupled with Prisma and PlanetScale (MySQL) for database efficiency, while integrating Stripe for payment processing and Tiptap for advanced text editing capabilities. 
    ChatPDF - SaaS Product ● Developed a SaaS platform with a dual-tier subscription model, utilizing Next.js, Tailwind CSS, and TypeScript for a seamless user interface, enabling PDF uploads for proprietary data training, and efficient information extraction via an LLM model. ● Facilitated streamlined data processing through a user-centric platform, significantly minimizing time spent on information retrieval from PDFs, while ensuring transaction security with Stripe integration.
    """
jt = st.text_input("Job Title: ", key="jt")
jd = st.text_area("Job Description: ", key="jd")
ques = st.text_input("Question: ", key="ques")

on = st.toggle("Copy details")

if on:
    col4, col5, col6, col8 = st.columns(4)

    with col4:
        lin = st.button("Linkedin")

    with col5:
        per = st.button("Personal")

    with col6:
        git = st.button("Github")
    with col8:
        email_template = st.button("Email Template")

    if lin:
        st_copy_to_clipboard("https://www.linkedin.com/in/dhruvsanan01/")
        st.success('Text copied successfully!')

    if per:
        st_copy_to_clipboard("https://dhruvsanan.vercel.app")
        st.success('Text copied successfully!')

    if git:
        st_copy_to_clipboard("https://github.com/dhruvsanan")
        st.success('Text copied successfully!')
    if email_template:
        st_copy_to_clipboard("""Dear Colby and Nisar,

I'm writing to express my strong interest in the Chief Technology Officer and Co-Founder position at ReFocus AI. Your mission to leverage AI for improving customer retention in the insurance industry deeply resonates with me. My background in both AI development and building full-stack SaaS applications makes me a perfect fit to lead your engineering team and contribute to ReFocus AI's growth.

In my previous role at Nvision Soft (Miami, Florida), I spearheaded the development of a smart Applicant Tracking System (ATS) that reduced hiring time by 60%. This project highlights my ability to deliver data-driven solutions that significantly impact business goals. 

I'm also eager to highlight my personal projects that demonstrate my understanding of LLMs:

AI Lead Magnet (SaaS Product): I spearheaded the development of a full-stack AI application that transforms content into interactive AI lead magnets. This project involved leveraging Langchain models to create a dynamic and engaging user experience.
ChatPDF (SaaS Product): I built a SaaS platform utilizing Next.js and OpenAI's capabilities. This platform allows users to upload PDFs for proprietary data training and efficient information extraction through an LLM model. My work focused on optimizing the LLM integration for seamless data processing and user experience.
Video Analyser project: I pushed the boundaries of AI capabilities by developing a video analysis tool before Gemini Pro could accept video inputs. This project utilized cutting-edge techniques:
Computer Vision: I leveraged computer vision libraries to extract individual frames from the video stream.
OpenAI's Whisper Model API: I integrated OpenAI's Whisper AI's API to analyse the spoken dialogue. This allowed me to analyze the video content based on both the visual information and the spoken dialogue.
This project demonstrates my ability to not only develop AI solutions but also translate them into user-centric applications that address real-world problems – a skillset directly applicable to ReFocus AI's mission.

Having thrived in a remote environment at Nvision Soft (Miami, Florida), I'm confident in seamlessly integrating into your team and collaborating effectively across time zones. My strong communication skills and ability to explain complex technical concepts ensure clear collaboration within the team and with external partners.

I'm eager to discuss how my expertise in AI development, full-stack development, and a passion for building impactful solutions can contribute to ReFocus AI's success. I'm available for a call at your earliest convenience.

Thank you for your time and consideration. I've included a link to my calendar for scheduling convenience: 

Calendar

Sincerely,

Dhruv Sanan
+91-7901919447 |  Personal Website""")
        st.success('Text copied successfully!')
else:
    col1, col2, col3, col7 = st.columns(4)

    with col1:
        email = st.button("Email")

    with col2:
        cl = st.button("Cover Letter")

    with col3:
        q = st.button("Q&A")

    with col7:
        qa = st.button("Resume Q&A")


# clear_button = st.button("Clear Results")
# if clear_button:
#     st.session_state['email'] = []
#     st.session_state['cl'] = []
#     st.session_state['q'] = []

if 'q' not in st.session_state:
    st.session_state['q'] = []

if 'qa' not in st.session_state:
    st.session_state['qa'] = []

if 'cl' not in st.session_state:
    st.session_state['cl'] = []

if 'email' not in st.session_state:
    st.session_state['email'] = []

show_answer = st.button("Show Answer")
if show_answer:
    if 'q' in st.session_state:
        st.write(q)

    if 'qa' in st.session_state:
        st.write(qa)

    if 'cl' in st.session_state:
        st.write(cl)

    if 'email' not in st.session_state:
        st.write(email)

email_template = """Dear Colby and Nisar,

I'm writing to express my strong interest in the Chief Technology Officer and Co-Founder position at ReFocus AI. Your mission to leverage AI for improving customer retention in the insurance industry deeply resonates with me. My background in both AI development and building full-stack SaaS applications makes me a perfect fit to lead your engineering team and contribute to ReFocus AI's growth.

In my previous role at Nvision Soft (Miami, Florida), I spearheaded the development of a smart Applicant Tracking System (ATS) that reduced hiring time by 60%. This project highlights my ability to deliver data-driven solutions that significantly impact business goals. 

I'm also eager to highlight my personal projects that demonstrate my understanding of LLMs:

AI Lead Magnet (SaaS Product): I spearheaded the development of a full-stack AI application that transforms content into interactive AI lead magnets. This project involved leveraging Langchain models to create a dynamic and engaging user experience.
ChatPDF (SaaS Product): I built a SaaS platform utilizing Next.js and OpenAI's capabilities. This platform allows users to upload PDFs for proprietary data training and efficient information extraction through an LLM model. My work focused on optimizing the LLM integration for seamless data processing and user experience.
Video Analyser project: I pushed the boundaries of AI capabilities by developing a video analysis tool before Gemini Pro could accept video inputs. This project utilized cutting-edge techniques:
Computer Vision: I leveraged computer vision libraries to extract individual frames from the video stream.
OpenAI's Whisper Model API: I integrated OpenAI's Whisper AI's API to analyse the spoken dialogue. This allowed me to analyze the video content based on both the visual information and the spoken dialogue.
This project demonstrates my ability to not only develop AI solutions but also translate them into user-centric applications that address real-world problems – a skillset directly applicable to ReFocus AI's mission.

Having thrived in a remote environment at Nvision Soft (Miami, Florida), I'm confident in seamlessly integrating into your team and collaborating effectively across time zones. My strong communication skills and ability to explain complex technical concepts ensure clear collaboration within the team and with external partners.

I'm eager to discuss how my expertise in AI development, full-stack development, and a passion for building impactful solutions can contribute to ReFocus AI's success. I'm available for a call at your earliest convenience.

Thank you for your time and consideration. I've included a link to my calendar for scheduling convenience: 

Calendar

Sincerely,

Dhruv Sanan
+91-7901919447 |  Personal Website"""
email_prompt = """ You are an expert in creating professional emails
                I have provided you with resume and jd. 
                create an email to founder explaining why are you a good fit for given position. 
                the first few sentences should explain why are you a great fit for the job, 
                the second part should be an interesting part about you that related to the job so that they can see you know what you're talking about. 
                then you should talk about your previous experience at NvisionSoft where you Automated resume review, enabling the processing of over 150 resumes per hour. Applied advanced relevance techniques to shortlist the top 10% of candidates, ensuring high-quality hires and improved talent acquisition outcomes through cross-functional teamwork.
                then talk about ChatPDF, your project in the resume. 
                Also give them confidence and you have already worked with a company in US so time difference isn't really a problem for you. 
                Also, you are willing to relocate if necessary.
                make sure that the email is interesting and eye catching, demonstrating your skills and experience and how can you contribute to the company if given the job.
                make sure to follow the follwing template
                """
cl_prompt = """create a cover letter for this job using below format 
                Greetings to the hiring team

                I am writing to express my strong interest in the XYZ role at ABC. With a comprehensive background in BLA BLA, I am enthusiastic about contributing to [ORG’s Name] mission of enhancing its [MISSION-whatever it may be].
                Intro- Use a catchy hook
                [2 lines- why you are interested/ your biggest achievement and how it relates to the role]- Ideally keep this generic since it will be recycled for 100s of apps.

                Work Ex
                Key work exs- Key project within each, how it relates to the job, and what you delivered in each job - USE NUMBERS
                Extra Curricular- But professional
                Talk about publications, awards, founding experience, teaching experience (Refer your CV)
                Your Commitment
                Write your heart out, we will edit it.

                With nearly [EXP] years immersed in the [YOUR INDUSTRY] realm, I possess a deep understanding of its nuances. My blend of hands-on experience, academic proficiency, strong work ethic, and genuine passion positions me as an ideal fit for thriving in the dynamic and stimulating environment at [ORG].

                Once again, thank you for considering my application. I look forward to the opportunity to discuss how my skills and experiences align perfectly with [org’S] goals.

                Best regards,

                Name
                Make sure to talk about your previous experience at NvisionSoft where you Automated resume review, enabling the processing of over 150 resumes per hour. Applied advanced relevance techniques to shortlist the top 10% of candidates, ensuring high-quality hires and improved talent acquisition outcomes through cross-functional teamwork.
                """
q_prompt = """Using the Jd and resume, Answer the question in an interesting and eye catching way demonstrating your skills and experience and how can you contribute to the company if given the job."""
qa_prompt = """Using resume, Answer the question in an interesting and eye catching way demonstrating your skills and experience and how can you contribute to the company if given the job. Your answer should reflect your personality."""

if email:
    if jt and jd:
        email = get_gemini_response(pdf_content, jt, jd, email_prompt)
        st.session_state['email'] = email
        st.write(email)
    else:
        st.write("Please write JT and JD")
if cl:
    if jt and jd:
        cl = get_gemini_response(pdf_content, jt, jd, cl_prompt)
        st.session_state['cl'] = cl
        st.write(cl)
    else:
        st.write("Please write JT and JD")
if q:
    if jt and jd:
        q = get_gemini_response(pdf_content, jt, jd, q_prompt+ques)
        st.session_state['q'] = q
        st.write(q)
    else:
        st.write("Please write JT and JD")
if qa:
    model = genai.GenerativeModel('gemini-1.5-pro-latest')
    qa = model.generate_content([pdf_content, qa_prompt+ques])
    st.session_state['qa'] = qa
    st.write(qa)
