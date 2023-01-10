import streamlit as st
from ums import User
from localStoragePy import localStoragePy

st.set_page_config(page_title='UMS', page_icon='🙂')
localStorage = localStoragePy('lpuums.streamlit.app', 'sqlite')

def details(regno,password):
    user = User(registration=regno, password=password)

    with st.container():

        #user info
        profile=user.user_profile()
        if 'data' in profile:
            st.header("Welcome " + profile["data"]["Name"]["Full Name"] + " :wave:")
            with st.expander("User Details", expanded=True):
                st.info("Registration No: " + profile["data"]["RegNo"])
                st.info("Roll No : " + profile["data"]["Rollno"])
                st.info("Term: " + profile["data"]["Term"])
                st.info("Section: " + profile["data"]["Section"])
                st.info("Programme: " + profile["data"]["Programme"])
                st.info("Books Issued: " + profile["data"]["Books Issued"])
        else:
            st.write("Failed to load Profile")
        
        # Classes
        d=st.container()
        d.title("Time Table")
        classes = user.classes()
        if 'message' in classes["data"][0].keys() :
            st.write(classes["data"][0]["message"])
        else:
            for i in classes["data"]:
                st.title(i["course"])
                st.info("Timing: " + i["timing"])
                st.info("Platform/Room: " + i["platform"])
                st.info("Status: " + i["status"])

        #messages
        messages = user.messages()
        c=st.container()
        c.title("Latest Messages")
        for i in messages['data']:
            with st.expander(i["subject"]):
                st.info(i["body"])

        #announcements
        announcements = user.annoucements()
        f=st.container()
        f.title("Announcents")
        f.caption("It displays only 10 at this moment")
        for i in announcements["data"]:
            with st.expander(i["title"]):
                st.info(i["body"])
                    
        # Datesheet
        datesheet = user.datesheet()
        e=st.container()
        e.title("Datesheet")
        if 'message' in datesheet.keys() :
            st.write(datesheet["message"])
        else:
            for i in range(5):
                st.title(datesheet["data"][i]["c_code"] + " - " + datesheet["data"][i]["course"])
                st.write("Reporting Timing" + datesheet["data"][i]["report"])
                st.write("Exam Timing" + datesheet["data"][i]["timing"])
        
        #marks
        f=st.container()
        f.title("Marks")
        marks = user.marks()
        for a in marks["data"]:
            with st.expander("TermID : " + a["termid"]):
                a=a["courses"]
                for i in a:
                    st.write(i["course"])
                    i=i["marks"]
                    for j in i:

                        st.success(j["type"] + " Marks : " + j["marks"][1])

        #Grades
        grades = user.grades()
        g=st.container()
        g.title("Grades")
        for i in grades["data"]:
            with st.expander("Term " + str(i["term"])):
                st.write("TGPA: " + str(i["tgpa"]))
                for j in i["grades"]:
                    st.success(j["course"]+ ": " + j["grade"])


def details1(regno,password):
    user = User(registration=regno, password=password)

    with st.container():

        #user info
        profile=user.user_profile()
        if 'data' in profile:
            st.header("Welcome " + profile["data"]["Name"]["Full Name"] + " :wave:")
            with st.expander("User Details"):
                st.info("Registration No: " + profile["data"]["RegNo"])
                st.info("Roll No : " + profile["data"]["Rollno"])
                st.info("Term: " + profile["data"]["Term"])
                st.info("Section: " + profile["data"]["Section"])
                st.info("Programme: " + profile["data"]["Programme"])
                st.info("Books Issued: " + profile["data"]["Books Issued"])
        else:
            st.write("Failed to load Profile")
        
        # Classes
        d=st.container()
        d.title("Time Table")
        classes = user.classes()
        if 'message' in classes["data"][0].keys() :
            st.write(classes["data"][0]["message"])
        else:
            for i in classes["data"]:
                st.title(i["course"])
                st.info("Timing: " + i["timing"])
                st.info("Platform/Room: " + i["platform"])
                st.info("Status: " + i["status"])

        #messages
        messages = user.messages()
        c=st.container()
        c.title("Latest Messages")
        for i in messages['data']:
            with st.expander(i["subject"]):
                st.info(i["body"])

        #announcements
        announcements = user.annoucements()
        f=st.container()
        f.title("Announcents")
        f.caption("It displays only 10 at this moment")
        for i in announcements["data"]:
            with st.expander(i["title"]):
                st.info(i["body"])
                    
        # Datesheet
        datesheet = user.datesheet()
        e=st.container()
        e.title("Datesheet")
        if 'message' in datesheet.keys() :
            st.write(datesheet["message"])
        else:
            for i in range(5):
                st.title(datesheet["data"][i]["c_code"] + " - " + datesheet["data"][i]["course"])
                st.write("Reporting Timing" + datesheet["data"][i]["report"])
                st.write("Exam Timing" + datesheet["data"][i]["timing"])
        
        #marks
        f=st.container()
        f.title("Marks")
        marks = user.marks()
        for a in marks["data"]:
            with st.expander("TermID : " + a["termid"]):
                a=a["courses"]
                for i in a:
                    st.write(i["course"])
                    i=i["marks"]
                    for j in i:

                        st.success(j["type"] + " Marks : " + j["marks"][1])

        #Grades
        grades = user.grades()
        g=st.container()
        g.title("Grades")
        for i in grades["data"]:
            with st.expander("Term " + str(i["term"])):
                st.write("TGPA: " + str(i["tgpa"]))
                for j in i["grades"]:
                    st.success(j["course"]+ ": " + j["grade"])

        #Auto Login Function
        st.button(label="Logout", on_click=localStorage.clear())

def check_password():
    k1=localStorage.getItem('k1')
    k2=localStorage.getItem('k2')
    if k1==None or k2==None:
        placeholder = st.empty()
        with placeholder.form(key='my_form', clear_on_submit=False):
            regis = st.text_input(label='Enter Your Registration No: ',placeholder='1200xx' )
            userp = st.text_input(label='Enter Password', type="password" ,placeholder="Password Goes Here" ,)
            submit_button = st.form_submit_button(label='Submit')
            if submit_button:
                localStorage.setItem('k1',regis)
                localStorage.setItem('k2',userp)
                return details(regis,userp)
    else:
        return details1(k1,k2)

check_password()




