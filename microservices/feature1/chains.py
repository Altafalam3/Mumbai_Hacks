# In chains.py
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
import os
from dotenv import load_dotenv

load_dotenv()

class HealthcareChain:
    def __init__(self):
        self.llm = ChatGroq(
            temperature=0.2,
            groq_api_key=os.getenv("GROQ_API_KEY"),
            model_name="llama-3.2-90b-vision-preview"
        )

    def analyze_patient_case(self, patient_history, patient_image):
        prompt_healthcare = PromptTemplate.from_template(
            """
            ### PATIENT'S HISTORY:
            {patient_history}

            ### PATIENT'S MEDICAL IMAGE:
            {patient_image}

            ### INSTRUCTION:
            You are a highly experienced healthcare expert specializing in diagnostics and personalized care. Based on the patient's history and the attached medical image, provide the following in structured JSON format:

            1. `Diagnosis`: Summarize any potential diagnosis based on the patient's history and image analysis.
            2. `Recommended Tests`: Suggest any further tests or imaging studies required for a more precise diagnosis.
            3. `Treatment Plan`: Provide an initial treatment approach, mentioning any medications or therapies.
            4. `Follow-Up`: Specify follow-up intervals and any signs for immediate attention.
            
            ### RESPONSE FORMAT:
            {{
                "Diagnosis": "Your diagnosis here",
                "Recommended Tests": ["Test1", "Test2", ...],
                "Treatment Plan": "Your treatment approach here",
                "Follow-Up": "Your follow-up plan here"
            }}
            """
        )

        # Invoke the prompt chain for healthcare
        chain_healthcare = prompt_healthcare | self.llm
        response = chain_healthcare.invoke({"patient_history": patient_history, "patient_image": patient_image})

        # Parse the output as JSON
        try:
            json_parser = JsonOutputParser()
            response_data = json_parser.parse(response.content)
            return response_data
        except OutputParserException:
            raise OutputParserException("Unable to parse healthcare details.")
