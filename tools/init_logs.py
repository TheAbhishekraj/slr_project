import os

folders = [
    '00_scope',
    '01_data',
    '01_data/01_data_raw',
    '01_data/02_data_proceesed',
    '01_data/03_pdfs',
    '02_cards',
    '03_ai_checks',
    '04_master',
    '05_analysis',
    '06_manuscript',
    '07_certificates',
    'tools'
]

readme_template = "# {name}\n\nThis directory contains the {name} files for the SLR project.\n\n"
log_template = "# {name} Action Log\n\n| Date | Action | Performed By | Notes |\n| :--- | :--- | :--- | :--- |\n| 2026-10-02 | Initialized directory | Antigravity | Directory setup and log created. |\n"

for f in folders:
    if not os.path.exists(f):
        os.makedirs(f)
        
    readme_path = os.path.join(f, 'README.md')
    if not os.path.exists(readme_path):
        with open(readme_path, 'w', encoding='utf-8') as f_out:
            f_out.write(readme_template.format(name=os.path.basename(f)))
        print(f"Created {readme_path}")
        
    # Check for existing logs (any file with 'log' in name)
    has_log = False
    for filename in os.listdir(f):
        if 'log' in filename.lower() and (filename.endswith('.md') or filename.endswith('.csv')):
            has_log = True
            break
            
    if not has_log:
        log_path = os.path.join(f, 'action_log.md')
        with open(log_path, 'w', encoding='utf-8') as f_out:
            f_out.write(log_template.format(name=os.path.basename(f)))
        print(f"Created {log_path}")

print("Done ensuring README and Action Log files exist in all directory sections.")
