def read_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
    return content.lower().split()

resume_words = set(read_file("resume.txt"))
job_words = set(read_file("job_description.txt"))

matched_skills = resume_words.intersection(job_words)
missing_skills = job_words.difference(resume_words)

match_percentage = (len(matched_skills) / len(job_words)) * 100

print("Matched Skills:", matched_skills)
print("Missing Skills:", missing_skills)
print(f"Skill Match Percentage: {match_percentage:.2f}%")

with open("output.txt", "w") as file:
    file.write("Matched Skills: " + ", ".join(matched_skills) + "\n")
    file.write("Missing Skills: " + ", ".join(missing_skills) + "\n")
    file.write(f"Match Percentage: {match_percentage:.2f}%")
