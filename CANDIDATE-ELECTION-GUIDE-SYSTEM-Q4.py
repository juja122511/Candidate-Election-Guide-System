import customtkinter as ctk
from datetime import datetime
import os
import json

#appearance
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

#window
app = ctk.CTk()
app.geometry("600x600")
app.title("Candidate Election Guide System")

#admin password
ADMIN_PASSWORD = "admin123"

#----------CANDIDATE DATA----------

candidates = {

    "Ferdinand 'Bongbong' Marcos Jr.": {
        "running_mate": "Sara Duterte",
        "alignment": "Conservative nationalism, Political continuity, Alliance with supporters of Rodrigo Duterte, Strong executive leadership",
        "platform": "Post-pandemic economic recovery, Infrastructure expansion, Agricultural modernization, Energy development, Government digitalization",
        "policy": "Infrastructure investment, Food security, Farmer support",
        "slogan": "Unity",
        "message": "National cooperation, Political reconciliation",
        "history": "Former senator, Former Ilocos Norte governor and congressman, Son of Ferdinand Marcos"
    },

    "Leni Robredo": {
        "running_mate": "Francis 'Kiko' Pangilinan",
        "alignment": "Liberal democracy, Reformist governance, Transparency and accountability, Participatory politics",
        "platform": "Anti-corruption reforms, Healthcare expansion, Education access, Small business support, Inclusive economic growth",
        "policy": "Poverty reduction, Social welfare programs, Agricultural support, Community development",
        "slogan": "Angat Buhay Lahat",
        "message": "Inclusive progress, People-centered governance",
        "history": "Human rights lawyer, Camarines Sur congresswoman, Vice President (2016–2022)"
    },

    "Manny Pacquiao": {
        "running_mate": "Lito Atienza",
        "alignment": "Populist politics, Social conservatism, Religious influence, Pro-poor advocacy",
        "platform": "Anti-corruption campaign, Social housing expansion, Rural development, Agricultural investment",
        "policy": "Poverty alleviation, Welfare programs, Government accountability",
        "slogan": "Laban ng Mahirap",
        "message": "Advocacy for the poor",
        "history": "Professional boxing champion, International sports icon, Philippine senator (2016–2022)"
    },

    "Isko Moreno": {
        "running_mate": "Willie Ong",
        "alignment": "Centrist politics, Pragmatic governance, Technocratic leadership",
        "platform": "Economic recovery, Job creation, Healthcare strengthening, Housing programs, Urban infrastructure",
        "policy": "Efficient governance, Rapid policy implementation, Urban development",
        "slogan": "Bilis Kilos",
        "message": "Fast government action",
        "history": "Former actor, Vice mayor of Manila, Mayor of Manila"
    },

    "Panfilo Lacson": {
        "running_mate": "Tito Sotto",
        "alignment": "Law-and-order politics, Fiscal conservatism, Institutional reform",
        "platform": "Anti-corruption reforms, Budget transparency, National security strengthening, Law enforcement reform",
        "policy": "Government accountability, Public finance discipline, Security and policing",
        "slogan": "Aayusin ang Gobyerno",
        "message": "Government reform",
        "history": "Former chief of Philippine National Police, Long-time senator"
    },

    "Leody de Guzman": {
        "running_mate": "Walden Bello",
        "alignment": "Left-wing politics, Labor movement, Progressive activism, Economic redistribution",
        "platform": "Minimum wage increase, Workers’ rights protection, Public healthcare expansion, Free education, National industrialization",
        "policy": "Economic equality, Labor protection, Social welfare expansion",
        "slogan": "Honest governance",
        "message": "Worker empowerment",
        "history": "Labor activist, Trade union leader, Workers’ movement organizer"
    },

    "Ernesto Abella": {
        "running_mate": "Rizalito David",
        "alignment": "Conservative politics, Moral governance, National development focus",
        "platform": "Economic recovery, Job creation, Infrastructure development, Support for small businesses",
        "policy": "Ethical leadership, National unity, Economic modernization",
        "slogan": "Moral leadership",
        "message": "Responsible governance",
        "history": "Former presidential spokesperson, Evangelical Christian leader, Former communications secretary under Rodrigo Duterte"
    },

    "Norberto Gonzales": {
        "running_mate": "Manny SD Lopez",
        "alignment": "Conservative governance, Strong national security focus, Anti-communist stance",
        "platform": "National security strengthening, Military and defense modernization, Economic development",
        "policy": "Counterinsurgency, Internal security, Government stability",
        "slogan": "Security-first governance",
        "message": "National stability",
        "history": "Former national security adviser, Former defense secretary, Longtime security policy official"
    },

    "Faisal Mangondato": {
        "running_mate": "Carlos Serapio",
        "alignment": "Regional representation politics, Federalism advocacy, Mindanao development focus",
        "platform": "Federal system of government, Regional autonomy expansion, Economic development in underserved regions",
        "policy": "Mindanao economic growth, Decentralized governance, Regional equality",
        "slogan": "Inclusive national development",
        "message": "Empowering regions",
        "history": "Lawyer, Businessman, Political figure from Mindanao"
    },

    "Jose Montemayor Jr.": {
        "running_mate": "David D'Angelo",
        "alignment": "Reformist politics, Conservative social views, Anti-corruption advocacy",
        "platform": "Healthcare reform, Government accountability, Economic reform",
        "policy": "Medical system improvement, Anti-corruption enforcement, Public service reform",
        "slogan": "Honest governance",
        "message": "Public health priority",
        "history": "Physician, Health sector advocate, Former political candidate"
    }

}

#----------VOTE STORAGE----------

VOTE_FILE = "votes.json"

def load_votes():
    if os.path.exists(VOTE_FILE):
        with open(VOTE_FILE, "r") as f:
            return json.load(f)

    return {
        "Ferdinand 'Bongbong' Marcos Jr.": 1200,
        "Leni Robredo": 980,
        "Manny Pacquiao": 650,
        "Isko Moreno": 430,
        "Panfilo Lacson": 300,
        "Leody de Guzman": 200,
        "Ernesto Abella": 150,
        "Norberto Gonzales": 120,
        "Faisal Mangondato": 90,
        "Jose Montemayor Jr.": 60
    }

def save_votes():
    with open(VOTE_FILE, "w") as f:
        json.dump(votes, f)

# IMPORTANT: THIS ACTUALLY LOADS YOUR VOTES
votes = load_votes()

voter_registry = set()
#----------TITLE----------

title = ctk.CTkLabel(
    app,
    text="Candidate Election Guide System",
    font=("Arial", 26)
)
title.pack(pady=20)

#----------NOTICE----------

notice = ctk.CTkLabel(
    app,
    text="NOTICE: Only users 18 years old and above are allowed to vote."
)
notice.pack(pady=5)

#----------NAME FORMAT LABEL----------

name_format = ctk.CTkLabel(
    app,
    text="Enter Full Name in this format: First Name M. Last Name"
)
name_format.pack()

#----------FULL NAME ENTRY----------

name_entry = ctk.CTkEntry(app)
name_entry.pack(pady=10)

#----------BIRTH YEAR----------

birth_entry = ctk.CTkEntry(
    app,
    placeholder_text="Enter Birth Year (YYYY)"
)
birth_entry.pack(pady=10)

#----------ROLE SELECTION----------

def role_changed(choice):

    birth_year = birth_entry.get()

    if not birth_year.isdigit():
        password_label.pack_forget()
        password_entry.pack_forget()
        return

    age = datetime.now().year - int(birth_year)

    if choice == "Administrator":

        if age < 30:
            message.configure(text="Admins must be 30 years old or above.")
            password_label.pack_forget()
            password_entry.pack_forget()

        else:
            message.configure(text="")
            password_label.pack(pady=(10,0))
            password_entry.pack(pady=5)

    else:
        password_label.pack_forget()
        password_entry.pack_forget()
        message.configure(text="")

role_menu = ctk.CTkOptionMenu(
    app,
    values=["Voter","Administrator"],
    command=role_changed
)
role_menu.pack(pady=10)

#----------ADMIN PASSWORD----------

password_label = ctk.CTkLabel(
    app,
    text="Administrator Password"
)

password_entry = ctk.CTkEntry(
    app,
    show="*"
)

#----------MESSAGE LABEL----------

message = ctk.CTkLabel(app,text="")
message.pack(pady=10)

#----------CANDIDATE INFORMATION----------

def show_candidate_info(candidate):

    info_window = ctk.CTkToplevel(app)
    info_window.geometry("500x400")
    info_window.title(candidate)

    textbox = ctk.CTkTextbox(
        info_window,
        width=450,
        height=300
    )
    textbox.pack(pady=10)

    info_text = ""

    info_text += f"{candidate}\n\n"
    info_text += f"Running Mate: {candidates[candidate]['running_mate']}\n\n"
    info_text += f"Political Alignment: {candidates[candidate]['alignment']}\n\n"
    info_text += f"Platform: {candidates[candidate]['platform']}\n\n"
    info_text += f"Key Policy Focus: {candidates[candidate]['policy']}\n\n"
    info_text += f"Slogan: {candidates[candidate]['slogan']}\n\n"
    info_text += f"Campaign Message: {candidates[candidate]['message']}\n\n"
    info_text += f"Background: {candidates[candidate]['history']}\n"

    textbox.insert("0.0",info_text)


def open_candidate_information():

    selection_window = ctk.CTkToplevel(app)
    selection_window.geometry("400x450")
    selection_window.title("Select Candidate")

    title = ctk.CTkLabel(
        selection_window,
        text="Select a Candidate",
        font=("Arial",22)
    )
    title.pack(pady=20)

    for candidate in candidates:

        candidate_button = ctk.CTkButton(
            selection_window,
            text=candidate,
            command=lambda c=candidate: show_candidate_info(c)
        )
        candidate_button.pack(pady=5)

#----------VOTING SYSTEM----------

def open_voting():

    if name_entry.get().title() in voter_registry:
        message.configure(text="You have already cast your vote!")
        return

    vote_window = ctk.CTkToplevel(app)
    vote_window.geometry("400x450")
    vote_window.title("Vote")

    result = ctk.CTkLabel(vote_window,text="")
    result.pack(pady=10)

    def cast_vote(candidate):
        votes[candidate] += 1
        save_votes()

        voter_registry.add(name_entry.get().title())

        result.configure(text=f"You voted for {candidate}")

    for candidate in candidates:

        vote_button = ctk.CTkButton(
            vote_window,
            text=candidate,
            command=lambda c=candidate: cast_vote(c)
        )
        vote_button.pack(pady=5)

#----------CANDIDATE COMPATIBILITY SURVEY (MULTI-PAGE)----------

def open_survey():

    #questions and options
    questions = [
        {
            "question": "1. Which political alignment do you prefer?",
            "options": ["Conservative", "Liberal", "Centrist", "Left-wing", "Populist"]
        },
        {
            "question": "2. Which area of government should be prioritized?",
            "options": ["Economy", "Healthcare", "Infrastructure", "Security", "Education"]
        },
        {
            "question": "3. Do you prefer a candidate with experience or fresh perspective?",
            "options": ["Experienced", "Fresh perspective"]
        },
        {
            "question": "4. How important is moral/religious governance for you?",
            "options": ["Very important", "Somewhat important", "Not important"]
        },
        {
            "question": "5. Which type of leadership style do you prefer?",
            "options": ["Technocratic/Pragmatic", "Charismatic/Populist", "Law-and-order", "Progressive"]
        }
    ]

    user_answers = {}

    #function to open next question page
    def show_question(q_index):

        if q_index >= len(questions):
            calculate_compatibility()
            return

        question_window = ctk.CTkToplevel(app)
        question_window.geometry("500x400")
        question_window.title(f"Question {q_index+1}")

        q_label = ctk.CTkLabel(
            question_window,
            text=questions[q_index]["question"],
            font=("Arial", 18),
            wraplength=450
        )
        q_label.pack(pady=20)

        #variable to store selection
        var = ctk.StringVar(value="")

        for option in questions[q_index]["options"]:
            rb = ctk.CTkRadioButton(
                question_window,
                text=option,
                variable=var,
                value=option
            )
            rb.pack(anchor="w", padx=20, pady=5)

        def next_question():
            user_answers[q_index] = var.get()
            if var.get() == "":
                return  # do not proceed if nothing selected
            question_window.destroy()
            show_question(q_index + 1)

        next_btn = ctk.CTkButton(
            question_window,
            text="Next",
            command=next_question
        )
        next_btn.pack(pady=20)


    #function to calculate best match
    def calculate_compatibility():

        results = []

        for candidate, info in candidates.items():
            score = 0

            #political alignment match
            alignment_answer = user_answers.get(0,"")
            if alignment_answer and alignment_answer.lower() in info["alignment"].lower():
                score += 1

            #government priority match
            priority = user_answers.get(1,"")
            if priority:
                if priority == "Economy" and ("economic" in info["platform"].lower() or "infrastructure" in info["platform"].lower()):
                    score += 1
                if priority == "Healthcare" and "health" in info["platform"].lower():
                    score += 1
                if priority == "Infrastructure" and "infrastructure" in info["platform"].lower():
                    score += 1
                if priority == "Security" and "security" in info["platform"].lower():
                    score += 1
                if priority == "Education" and "education" in info["platform"].lower():
                    score += 1

            #experience/fresh perspective
            experience = user_answers.get(2,"")
            if experience:
                if experience == "Experienced" and "Former" in info["history"]:
                    score += 1
                if experience == "Fresh perspective" and "Former" not in info["history"]:
                    score += 1

            #moral/religious governance preference
            moral = user_answers.get(3,"")
            if moral == "Very important" and "Conservative" in info["alignment"]:
                score += 1
            if moral == "Somewhat important" and "Conservative" in info["alignment"]:
                score += 0.5  # partial match

            #leadership style
            leadership = user_answers.get(4,"")
            if leadership:
                if leadership.lower() in info["alignment"].lower() or leadership.lower() in info["platform"].lower():
                    score += 1

            results.append((score,candidate))

        #sort so highest score is at the top
        results.sort(key=lambda x: x[0], reverse=True)
        
        #get the highest score achieved
        max_score = results[0][0]
        
        #find all candidates tied for that score
        top_candidates = [cand for score, cand in results if score == max_score]

        if len(top_candidates) == 1:
            display_text = f"Your most compatible candidate is:\n\n{top_candidates[0]}"
        else:
            names_joined = " and ".join(top_candidates)
            display_text = f"It's a tie! You are most compatible with:\n\n{names_joined}\n\nYou can choose between those candidates."

        #display result page
        result_window = ctk.CTkToplevel(app)
        result_window.geometry("500x400")
        result_window.title("Survey Result")

        result_label = ctk.CTkLabel(
            result_window,
            text=display_text,
            font=("Arial", 22),
            wraplength=450
        )
        result_label.pack(pady=50)

    #start survey with first question
    show_question(0)

#----------ADMIN FUNCTIONS----------

def open_admin_tally():
    t_win = ctk.CTkToplevel(app)
    t_win.title("Admin Tally")
    for c, v in sorted(votes.items(), key=lambda x: x[1], reverse=True):
        ctk.CTkLabel(t_win, text=f"{c}: {v} votes").pack(anchor="w", padx=20)

def open_admin_remove():
    r_win = ctk.CTkToplevel(app)
    r_win.title("Remove Candidate")
    entry = ctk.CTkEntry(r_win, placeholder_text="Candidate Name", width=300)
    entry.pack(pady=20)
    def remove():
        name = entry.get()
        if name in candidates:
            del candidates[name]
            del votes[name]
            status.configure(text=f"Removed {name}")
        else:
            status.configure(text="Not found")
    ctk.CTkButton(r_win, text="Remove", command=remove, fg_color="#00008B").pack(pady=10)
    status = ctk.CTkLabel(r_win, text="")
    status.pack()

#----------MAIN PAGE----------

def open_main_page(name,role):

    main_window = ctk.CTkToplevel(app)
    main_window.geometry("500x500")
    main_window.title("Main Menu")

    welcome = ctk.CTkLabel(
        main_window,
        text=f"Welcome {name}",
        font=("Arial",22)
    )
    welcome.pack(pady=20)

    vote_button = ctk.CTkButton(
        main_window,
        text="1 - Vote",
        command=open_voting
    )
    vote_button.pack(pady=10)

    info_button = ctk.CTkButton(
        main_window,
        text="2 - View Candidate Information",
        command=open_candidate_information
    )
    info_button.pack(pady=10)

    survey_button = ctk.CTkButton(
        main_window,
        text="3 - Candidate Compatibility Survey",
        command=open_survey
    )
    survey_button.pack(pady=10)

    if role == "Administrator":
        ctk.CTkLabel(main_window, text="Admin Tools").pack(pady=10)
        ctk.CTkButton(main_window, text="View Tally", command=open_admin_tally, fg_color="#00008B").pack(pady=5)
        ctk.CTkButton(main_window, text="Remove Candidate", command=open_admin_remove, fg_color="#00008B").pack(pady=5)

    exit_button = ctk.CTkButton(
        main_window,
        text="4 - Exit",
        command=main_window.destroy,
        fg_color="#FF0000"
    )
    exit_button.pack(pady=10)

#----------LOGIN FUNCTION----------

def login():

    name = name_entry.get().title()
    birth_year = birth_entry.get()
    role = role_menu.get()

    if name == "" or birth_year == "":
        message.configure(text="Please complete all required fields.")
        return

    if not birth_year.isdigit():
        message.configure(text="Birth year must be a number.")
        return

    current_year = datetime.now().year
    age = current_year - int(birth_year)

    if age < 18:
        message.configure(text="Access denied: You must be at least 18 years old.")
        return

    if role == "Administrator":

        if age < 30:
            message.configure(text="Admins must be 30 years old or above.")
            return

        password = password_entry.get()

        if password != ADMIN_PASSWORD:
            message.configure(text="Incorrect administrator password.")
            return

        message.configure(text=f"Welcome Administrator {name}")
        open_main_page(name,role)

    else:

        message.configure(text=f"Welcome Voter {name}")
        open_main_page(name,role)


#----------LOGIN BUTTON----------

login_button = ctk.CTkButton(
    app,
    text="Login",
    command=login
)
login_button.pack(pady=20)

app.mainloop()
