#!/usr/bin/env python
# coding: utf-8

# In[31]:


from transformers import pipeline
import gradio as gr

# Load Hugging Face model (can take a few seconds the first time)
chatbot = pipeline("text2text-generation", model="google/flan-t5-base")

# Basic HR knowledge base
hr_knowledge_base = {
    "leave policy": "Employees are entitled to 12 casual leaves and 15 earned leaves per year.",
    "holiday list": "You can check the official 2025 holiday list on the HR portal.",
    "salary slip": "Salary slips can be downloaded from the internal HRMS portal.",
    "grievance redressal": "For grievances, please email hr.support@company.com.",
    "onboarding": "New employees should complete the onboarding forms and attend orientation.",
    "exit policy": "Please submit your resignation via the HR portal. Exit interviews are mandatory. and also you have to serve the notice period which is 60 days from your rag daue",
    "probation period": "The standard probation period is 6 months.",
     "HR contact": "You can contact the HR team at hr@company.com.",
    "apply for leave": "You can apply for leave through the employee portal or by emailing hr@company.com.",
    "leave policy": "Our leave policy includes casual leave, sick leave, earned leave, and optional holidays. Please refer to the employee handbook or contact HR for more details.",
    "get salary slip": "You can download your salary slip from the HR portal under the 'Payslips' section. For any issues, email payroll@company.com.",
    "update personal information": "You can update your details via the HRMS portal or email hr@company.com.",
    "pf or tax query": "For PF or tax-related questions, please email payroll@company.com or contact the Payroll Helpdesk.",
    "request letter": "To request an official letter (employment, visa, bank), submit a request on the HR portal or email hrdocs@company.com.",
    "salary credit date": "Salaries are usually credited on the last working day of the month. HR will notify you of any delays.",
    "resignation process": "To resign, submit your resignation on the HR portal or inform your manager and HR. The standard notice period applies as per your contract.",
    "escalate issue": "For sensitive issues or concerns, contact hr@company.com or speak directly to an HR representative in confidence."""

}

# HR bot function
def hr_bot(query):
    # Try keyword match first
    for key in hr_knowledge_base:
        if key in query.lower():
            return hr_knowledge_base[key]
    
    # Otherwise use LLM
    prompt = f"You are an HR help desk assistant. Answer this politely:\n\n{query}\n\nAnswer:"
    result = chatbot(prompt, max_length=200, do_sample=True)[0]["generated_text"]
    return result.strip()

# Gradio app
gr.Interface(
    fn=hr_bot,
    inputs="text",
    outputs="text",
    title="HR Help Desk Chatbot",
    description="Ask HR-related questions like leave, holidays, salary slip, grievance, etc."
).launch()


# In[ ]:




