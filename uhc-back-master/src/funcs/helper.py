import openai

# Set your API key here
openai.api_key = "your-openai-api-key"

def generate_job_description(job_title):
    prompt = f"Write a detailed, professional job description for the role: {job_title}. Include responsibilities, required skills, and qualifications."

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[
            {"role": "system", "content": "You are a helpful assistant that writes HR-standard job descriptions."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=500
    )

    return response.choices[0].message["content"]

# Example usage
if __name__ == "__main__":
    job_title = input("Enter job title: ")
    description = generate_job_description(job_title)
    print("\nGenerated Job Description:\n")
    print(description)