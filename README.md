<body>
<h1>PES Jackfruit Problem</h1>
<p>
A Python-based command-line healthcare application that performs age group analysis, symptom-based illness checking, BMI calculation, and appointment token generation using CSV data.<br><br>
</p>

<h2>Healthcare Management & Symptom Analysis System (Python)</h2>
<p>
This project is a Python-based command-line healthcare application developed as an academic mini project. It combines patient data analysis, basic illness symptom checking,   BMI calculation, and appointment token generation into a single integrated program. The application is designed to demonstrate the use of Python programming, CSV file handling, conditional logic, and data analysis using Pandas in a healthcare-related context.<br><br>
</p>
 
<h2>Features</h2>
<h3>Age Group Analysis</h3>
  <ul>
  <li>Reads patient data from a CSV file (fake_patient.csv)</li>
  <li>Categorizes patients into predefined age groups: Child, Teen, Young Adult, Middle Age, Senior</li>
  <li>Displays:
    <ol>
    <li>Age group distribution</li>
    <li>Percentage of patients in each group</li>
    </ol>
  </li>
  </ul>
  <p><br></p>
  
<h3>Appointment Token Generator</h3>
  <ul>
  <li>Accepts number of patients and their names</li>
  <li>Automatically assigns sequential appointment tokens</li>
  <li>Saves the token list to a CSV file (AppointmentTokens.csv)</li>
  <li>Useful for managing patient queues</li>
  </ul>
<p><br></p>
  
<h3>General Illness Symptom Checker</h3>
  <ul>
  <li>Interactive symptom-based checker using user input</li>
  <li>Asks questions related to:
   <ol>
    <li>Fever, cough, cold</li>
    <li>Gastric symptoms</li>
    <li>Dengue-like symptoms</li>
    <li>Dehydration indicators</li>
    <li>Emergency red flags</li>
   </ol>
  </li>
  
  <li>Uses rule-based logic to identify the closest matching illness</li>
  <li>Provides general health advice</li>
  <li>Includes a clear medical disclaimer</li>
  </ul>
  <p>⚠ <b>Disclaimer</b><br><i>This tool is for educational purposes only and is not a replacement for professional medical diagnosis.</i></p>
  <p><br></p>
  
  <h3>⚖ BMI (Body Mass Index) Calculator</h3>
  <ul>
    <li>Calculates BMI using user height and weight</li>
    <li>
      Supports unit conversion:
      <ul>
      <li>kg ↔ lbs</li>
      <li>cm ↔ meters</li>  
      </ul>
    </li>
  
  <li>Categorizes BMI into:
   <ul>
    <li>Underweight</li>
    <li>Normal weight</li>
    <li>Overweight</li>
    <li>Obese</li>
   </ul>
  </li>

  <li>Displays:
  <ul>
  <li>BMI value</li>
  
  <li>BMI category (with colored terminal output)</li>
  
  <li>Ideal weight range</li>
  
  <li>Personalized lifestyle suggestions</li>
  </ul>   
  </ul>
  <p><br></p>
  
  <h2>Technologies Used</h2>
  <ol>
  <li>Python</li>
  <li>Pandas – CSV file handling and data analysis</li>
  <li>Command Line Interface (CLI)</li>
  <li>CSV files – Data input and output</li>
  </ol>
  <p><br></p>
  
  <h2>Project Highlights</h2>
  <ul>
    <li>Modular structure with reusable functions</li>
    <li>Demonstrates real-world healthcare use cases</li>
    <li>Uses conditional logic to simulate medical decision-making</li>
    <li>Includes data storage and retrieval using CSV files</li>
    <li>Terminal-based UI with colored output for better readability</li>
  </ul>
  
  <p>⚠ <b>Disclaimer</b><br>
  
  <i>
  This project is intended only for educational purposes.
  It does not provide medical diagnosis and should not be used for real medical decisions.
  Always consult a qualified healthcare professional for medical concerns.
  </i>
  </p>
  <p><br></p>
  <h2>How to Run the Project</h2>
  <ol>
  <li>
  Install required dependency using the command given below:
    
    pip install pandas
  </li>
  
  <li>Ensure fake_patient.csv is present in the same directory</li>
  <p><br></p>
  <li>Run the program:</li>
  
    python app.py
  </ol>
  <h2>Team Project</h2>
  <p>This project was developed collaboratively as part of an academic mini project to demonstrate Python programming concepts and basic healthcare data analysis. Team members:     <br>
  Aadi - <a href="https://github.com/Aadi-droid">Visit Github</a><br>
  Aishwarya - <a href="https://github.com/aish5mohan">Visit Github</a><br>
  Aditi - <a href="https://github.com/Aditisajjan">Visit Github</a><br>
  Akshara - <a href="https://github.com/aksharaazhagesan-creator">Visit Github</a><br>
  </p>

  <h2>Sample Output</h2>
  <img src="data:image/png;base64,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">
  </body>
