# phase_01.py - Core LLM initialization + Memory recall system

from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from datetime import datetime
import json
from pathlib import Path

# Load model and tokenizer (TPU-safe or CPU/GPU fallback)
model_id = "mistralai/Mistral-7B-Instruct-v0.1"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id)
generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

# Memory file setup
memory_file = Path("soulmate_memory.json")
if not memory_file.exists():
    memory_file.write_text("[]")

# Load memory
def load_memory():
    return json.loads(memory_file.read_text())

# Save memory
def save_memory(memory):
    memory_file.write_text(json.dumps(memory, indent=2))

# Log interaction
def log_interaction(user_input, response):
    memory = load_memory()
    memory.append({
        "timestamp": datetime.now().isoformat(),
        "user": user_input,
        "soulmate": response
    })
    save_memory(memory)

# Generate from model
def soulmate_response(prompt):
    output = generator(prompt, max_new_tokens=128, temperature=0.7)[0]["generated_text"]
    return output.split("### Response:")[-1].strip()
