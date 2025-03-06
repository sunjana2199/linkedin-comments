import pandas as pd


df = pd.read_csv("/Users/sunjana.rc/Documents/GitHub/linkedin-comments/linkedin-2025-03-05 (1).csv")
df = df[df['wkQoCItOvqHdCRxuwKdNtGbXtUZMSMuRJlBQg'].str.contains('@', na=False)]
df = df.rename(columns={'wkQoCItOvqHdCRxuwKdNtGbXtUZMSMuRJlBQg': 'email'})
df = df.rename(columns={'comments-comment-meta__description-title': 'name'})
df2 = df[['name', 'email']]
df['first_name'] = df['name'].str.split().str[0].str.capitalize()

# Create the final DataFrame with only first name and email
df2 = df[['first_name', 'email']]

df2.to_csv("linkedin_comments_March3.csv", index=False)