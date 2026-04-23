PROJECT FUNCTIONALITY

This project is an interactive web dashboard developed for Grazioso Salvare, an international rescue animal training company. The dashboard interfaces with a MongoDB database containing over 10,000 animal outcomes from the Austin Animal Center. The application allows users to filter this data to identify dogs that fit specific search-and-rescue profiles (Water Rescue, Mountain/Wilderness Rescue, and Disaster/Individual Tracking).
The dashboard features an interactive data table with pagination and sorting, a dynamic pie chart displaying the breed breakdown of the filtered data, and a geolocation map that updates to show the specific location of any animal selected in the data table.

FUNCTIONALITY PROOF

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

TOOLS AND RATIONALE

This application was built using a Model-View-Controller (MVC) software design pattern to ensure clean separation between the database, the user interface, and the logic connecting them.

  The Model: Mongodb

  MongoDB is a NoSQL, document-oriented database. It was chosen as the model component for this project because animal shelter data is often semi-structured and hierarchical. Unlike a rigid relational SQL database, MongoDB stores data in flexible, JSON-like BSON documents. This is incredibly advantageous when interfacing with Python, as MongoDB documents map directly to Python dictionaries. This native compatibility allows for seamless data manipulation using Python libraries like Pandas.
  
  The View And Controller: Dash Framework
  
  The Dash framework was utilized to construct both the View and Controller components of the application. Acting as the View, Dash enables the creation of responsive web user interfaces—such as the layout, interactive DataTable, and filter controls—using pure Python, eliminating the need to write raw HTML or JavaScript. Simultaneously, Dash functions as the Controller through its @app.callback decorators. These callbacks actively monitor user interactions, such as selecting a radio button or a table row, to trigger the appropriate MongoDB queries via the Python CRUD module. Once the data is retrieved, the controller seamlessly pushes the updated information back to the visual components, dynamically updating the pie chart and geolocation map.


DEVELOPMENT PROCESS

1.	DATABASE CONFIGURATION: The project began by setting up the MongoDB environment and importing the aac.animals dataset.
2.	CRUD MODULE DEVELOPMENT: A custom Python module was written to handle secure connections to the database and execute Create, Read, Update, and Delete operations using pymongo.
3.	UI LAYOUT (VIEW): Inside a Jupyter Notebook (JupyterDash), the visual components were arranged. This included branding (logo and developer identifier), filter controls, a paginated data table, a Plotly pie chart, and a Dash Leaflet map.
4.	WIRING THE CALLBACKS (CONTROLLER): Callback functions were written to execute specific MongoDB queries based on the user's radio button selection. Additional callbacks were linked to the DataTable so that the charts dynamically reacted to the data currently visible on the screen.

CHALLENGES ENCOUNTERED AND OVERCOME

One significant technical challenge occurred while linking the DataTable to the Geolocation map. Initially, if a user clicked on a high-index row (e.g., row 8) in the unfiltered table, and then applied a strict filter like "Water Rescue" (which only returned 5 total rows), the application would crash. The callback was trying to map a row index that no longer existed in the newly filtered dataset.

RESOLUTION: This was overcome by adding index-checking logic within the update_map callback. By converting the viewData into a Pandas DataFrame (dff), I could dynamically check the length of the new dataset (len(dff)). If the previously selected row index was greater than or equal to the new length of the dataframe, the logic forced the index to reset to 0. This prevented out-of-bounds errors and kept the dashboard stable during rapid filtering.

REFLECTION

Maintainability, Readability, and Adaptability

Writing maintainable and readable code requires a modular approach where specific tasks are isolated into independent scripts. In Project One, I developed a standalone Python CRUD module to handle all interactions with the MongoDB database. The primary advantage of this strategy was the decoupling of data logic from the user interface. Because the CRUD operations were self-contained, I was able to simply import that module into Project Two to power the dashboard widgets without rewriting any database connection logic. This adaptability is crucial in professional environments; if Grazioso Salvare eventually decided to migrate their data to a different database system, I would only need to update the single CRUD module rather than refactoring the entire dashboard application. In the future, this same module could be repurposed to power a mobile application or a back-end reporting tool for the same dataset.

The Computer Science Approach

As a computer scientist, my approach to solving the requirements for Grazioso Salvare was rooted in requirements analysis and iterative design. I began by breaking down the client’s request into two distinct functional needs: secure data management and intuitive data visualization. This project differed from previous assignments by requiring a seamless integration of multiple technologies—MongoDB, Python, and the Dash framework—into a singular, cohesive ecosystem. While earlier coursework often focused on isolated algorithms, this project demanded an "architectural" mindset, considering how data flows from a document store into a front-end visualization. In the future, I will continue to use the strategy of building a robust "Model" layer first, ensuring the data integrity is sound before building the visual "View" layer, which allows for more efficient testing and debugging.

The Role and Impact of Computer Scientists

Computer scientists serve as the bridge between raw data and actionable insights. By building tools like this dashboard, we enable organizations to transform thousands of disorganized records into a clear, visual narrative. For a company like Grazioso Salvare, this work matters because it directly impacts operational efficiency. Instead of manually searching through 10,000 animal outcomes, staff can now identify suitable search-and-rescue candidates in seconds. This speed allows the organization to fulfill its mission more effectively, saving both time and resources while ultimately improving the outcomes for the animals in their care. Our role is to create the systems that make complex tasks manageable, allowing experts in other fields to do their jobs with greater precision and confidence.

