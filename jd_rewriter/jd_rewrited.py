import yaml
from openai import OpenAI
from schema import RewriteResponse

with open("prompts.yaml", "r") as f:
    config = yaml.safe_load(f)

SYSTEM_PROMPT = config["SYSTEM_PROMPT"]
FEW_SHOT_PROMPT = config["FEW_SHOT_EXAMPLES"]
CONCISE_PROMPT = config["CONCISE_PROMPT"]
DETAILED_PROMPT = config["DETAILED_PROMPT"]

client = OpenAI(api_key="your_openai_api_key_here")  # Replace with your actual OpenAI API key

def generate_completion(prompt: str, temperature: float) -> str:
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "system", "content": SYSTEM_PROMPT},
                  {"role": "user", "content": FEW_SHOT_PROMPT + "\n\n" + prompt}],
        temperature=temperature,
    )
    return response.choices[0].message.content.strip()

def rewrite_jd(job_description: str, temperature: float=0.2):
    concise_prompt = CONCISE_PROMPT.format(job_description=job_description)
    detailed_prompt = DETAILED_PROMPT.format(job_description=job_description)
    concise_jd = generate_completion(concise_prompt, temperature)
    detailed_jd = generate_completion(detailed_prompt, temperature)
    return RewriteResponse(concise_version=concise_jd, detailed_version=detailed_jd)