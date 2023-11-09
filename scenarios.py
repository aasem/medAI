scenarios = {
    "Patient Medical Record Summarization": {
        "Use Case": "Summarizes lengthy patient records into concise reports.",
        "Input": "Full patient EHR text data.",
        "Output": "A short summary highlighting key points from the patient’s history.",
        "Design": "Simple prompt engineering with pre-trained LLMs.",
        "Complexity": "Low"
    },
    "Differential Diagnosis Assistance": {
        "Use Case": "Suggests potential diagnoses based on symptoms described.",
        "Input": "Symptom descriptions and patient history.",
        "Output": "A list of possible conditions and suggested tests.",
        "Design": "Fine-tuning a model on medical diagnosis data.",
        "Complexity": "High"
    },
    "Clinical Guideline Retrieval": {
        "Use Case": "Retrieves relevant clinical guidelines based on a medical query.",
        "Input": "Query related to a specific condition or treatment.",
        "Output": "The most pertinent clinical guideline or treatment protocol.",
        "Design": "RAG using indexed medical guideline documents.",
        "Complexity": "Medium"
    },
    "Drug Interaction Information": {
        "Use Case": "Provides information on drug interactions.",
        "Input": "List of patient medications.",
        "Output": "Information about potential drug interactions.",
        "Design": "Simple prompt engineering using a database of drug interactions.",
        "Complexity": "Low"
    },
    "Research Paper Information Retrieval": {
        "Use Case": "Answers queries by pulling information from medical research papers.",
        "Input": "Natural language research-related questions.",
        "Output": "Relevant information extracted from research papers.",
        "Design": "RAG with a corpus of indexed medical papers.",
        "Complexity": "Medium"
    },
    "Radiology Image Annotations": {
        "Use Case": "Suggests annotations for radiology images based on AI analysis.",
        "Input": "Radiology images (X-rays, MRIs, etc.).",
        "Output": "Textual annotations describing findings.",
        "Design": "Integration of computer vision and LLMs.",
        "Complexity": "High"
    },
    "EHR Data Extraction and Organization": {
        "Use Case": "Extracts specific types of data from EHRs upon request.",
        "Input": "Unstructured EHR text.",
        "Output": "Structured information such as lab results or medication lists.",
        "Design": "Fine-tuning an LLM for NER and relation extraction.",
        "Complexity": "High"
    },
    "Zero-Shot Learning for Rare Diseases Information": {
        "Use Case": "Provides information on rare diseases not well-represented in training data.",
        "Input": "Questions about rare conditions.",
        "Output": "Descriptions and information related to rare diseases.",
        "Design": "Zero-shot learning using a powerful pre-trained LLM.",
        "Complexity": "Medium"
    },
    "Medical Billing and Coding": {
        "Use Case": "Automates the extraction of information for billing from medical documents.",
        "Input": "Medical procedure texts and notes.",
        "Output": "Relevant billing codes and descriptions.",
        "Design": "Fine-tuning a model on a dataset of medical billing records.",
        "Complexity": "High"
    },
    "Chatbot for General Medical Inquiries": {
        "Use Case": "Answers general medical questions from patients or staff.",
        "Input": "Natural language questions on medical topics.",
        "Output": "Accurate and understandable medical information.",
        "Design": "Simple prompt engineering with pre-trained LLMs.",
        "Complexity": "Low"
    },
    "Lab Result Interpretation": {
        "Use Case": "Interprets lab results and flags abnormal values.",
        "Input": "Lab result data.",
        "Output": "Interpretations and potential clinical significance of lab values.",
        "Design": "Fine-tuning or simple prompt engineering with rule-based flags.",
        "Complexity": "Medium"
    },
    "Treatment Outcome Prediction": {
        "Use Case": "Predicts patient outcomes based on treatment protocols.",
        "Input": "Patient data and treatment information.",
        "Output": "Predicted outcomes or prognosis.",
        "Design": "Fine-tuning a model on clinical outcome data.",
        "Complexity": "High"
    },
    "Medical Literature Q&A": {
        "Use Case": "Answers complex questions with references to medical literature.",
        "Input": "In-depth medical queries.",
        "Output": "Detailed answers with citations.",
        "Design": "RAG with an indexed database of medical literature.",
        "Complexity": "High"
    },
    "Medical Image Search": {
        "Use Case": "Finds similar case studies or images based on an uploaded medical image.",
        "Input": "Medical image.",
        "Output": "Similar images and related case information.",
        "Design": "Integration of computer vision with LLMs for text-based search.",
        "Complexity": "High"
    },
    "Health Risk Assessment": {
        "Use Case": "Assesses patient health risks based on lifestyle data.",
        "Input": "Patient lifestyle information and medical history.",
        "Output": "Risk assessment and recommendations.",
        "Design": "Simple prompt engineering using pre-trained LLMs.",
        "Complexity": "Low"
    },
}
