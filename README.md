# Full-Stack Rescue Animal Dashboard

An interactive full-stack web dashboard designed for Grazioso Salvare to streamline animal rescue data analysis. This application bridges raw database records with actionable insights, allowing shelter staff to identify search-and-rescue candidates in seconds.

### 🛠️ Core Technologies
* **Framework:** Dash (View & Controller)
* **Database:** MongoDB (Model)
* **Data Processing:** Python, Pandas, Pymongo
* **Visualization:** Plotly (Charts), Dash Leaflet (Geolocation)

### 🚀 Key Features
* **Dynamic Filtering:** Real-time data filtering for specific rescue profiles (Water, Mountain/Wilderness, Disaster/Tracking).
* **Interactive Visualization:** Includes a paginated DataTable, breed-breakdown pie charts, and responsive geolocation mapping.
* **Full-Stack MVC Architecture:** Modular design separating the database logic (Model) from the UI and application flow (View & Controller).
* **Robust Error Handling:** Implements dynamic index-checking logic to maintain application stability during rapid UI state changes and data filtering.

### 🧠 Architectural Design
The application utilizes an **MVC (Model-View-Controller)** pattern:
* **Model:** MongoDB provides a flexible, document-oriented storage solution, allowing for seamless mapping of semi-structured animal shelter data to Python dictionaries.
* **View:** Dash enables the construction of responsive, high-performance web interfaces using pure Python.
* **Controller:** Dash `@app.callback` decorators manage the application state, handling user interactions and triggering targeted database queries.

### 📈 Proof of Functionality
Default/Reset State:

 <img width="580" height="555" alt="image" src="https://github.com/user-attachments/assets/a6b377b9-2068-4d06-ba27-80b0cee21b4f" />

Water Rescue:

 <img width="572" height="548" alt="image" src="https://github.com/user-attachments/assets/7ce94c64-4f40-4b8f-88d2-6eaba4313bba" />

Mountain or Wildlife Rescue:

 <img width="572" height="549" alt="image" src="https://github.com/user-attachments/assets/ff7bc34e-44da-4332-891c-e16ca70b718e" />

Disaster of Individual Tracking:

 <img width="579" height="555" alt="image" src="https://github.com/user-attachments/assets/4bcfc200-ebb4-4e23-b792-537291ddc0a1" />

Map Interaction:

 <img width="596" height="548" alt="image" src="https://github.com/user-attachments/assets/dc2f8857-4cf4-4fe7-9c7f-316b9092248f" />
