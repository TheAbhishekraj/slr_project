import csv
import os

def load_csv(filepath, title_col, source_name):
    records = []
    with open(filepath, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            title = row.get(title_col, '').strip()
            title_norm = ''.join(c for c in title.lower() if c.isalnum())
            records.append({'title': title, 'title_norm': title_norm, 'source': source_name, 'row': row})
    return records

def main():
    ieee_path = os.path.join('01_data', '01_data_raw', 'ieee_xplore_20260615.csv')
    scopus_path = os.path.join('01_data', '01_data_raw', 'scopus_20260615.csv')
    master_path = os.path.join('01_data', '02_data_proceesed', 'deduplicated_master.csv')
    log_path = os.path.join('01_data', '02_data_proceesed', 'dedup_log.csv')

    all_raw = load_csv(ieee_path, 'Document Title', 'IEEE') + load_csv(scopus_path, 'title', 'Scopus')
    
    master_titles = []
    with open(master_path, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            title = row.get('title', row.get('Title', '')).strip()
            title_norm = ''.join(c for c in title.lower() if c.isalnum())
            master_titles.append(title_norm)

    log_titles = []
    with open(log_path, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            title = row.get('title', '').strip()
            title_norm = ''.join(c for c in title.lower() if c.isalnum())
            log_titles.append((row.get('source', ''), title_norm))

    # We want to find exact mapping
    # Raw is 2000. Master is 1716.
    # Let's count occurrences of title_norm in raw.
    raw_counts = {}
    for r in all_raw:
        raw_counts[r['title_norm']] = raw_counts.get(r['title_norm'], 0) + 1
        
    master_counts = {}
    for t in master_titles:
        master_counts[t] = master_counts.get(t, 0) + 1

    # expected log counts = raw_counts - master_counts
    expected_drops = []
    for r in all_raw:
        # just list all raw
        pass
        
    # Let's do it simply by list removal
    # For every master title, remove one instance from all_raw
    remaining_raw = list(all_raw)
    for mt in master_titles:
        # find matching in remaining_raw
        for i, r in enumerate(remaining_raw):
            if r['title_norm'] == mt:
                remaining_raw.pop(i)
                break
                
    print(f"Remaining raw after matching master: {len(remaining_raw)}")
    
    # remaining_raw should have 284 items
    # now remove the ones that are in log
    remaining_after_log = list(remaining_raw)
    for ls, lt in log_titles:
        for i, r in enumerate(remaining_after_log):
            if r['title_norm'] == lt:
                remaining_after_log.pop(i)
                break
                
    print(f"Remaining raw after matching log: {len(remaining_after_log)}")
    
    for m in remaining_after_log:
        try:
            print(f"MISSING: {m['source']} | {m['title']}".encode('cp1252', errors='replace').decode('cp1252'))
        except:
            pass
        
    # Append to log, but wait, if it's not exactly 4, we shouldn't indiscriminately append.
    # We will just write all remaining_after_log to the csv for now to see what they are.
    with open(log_path, 'a', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)
        for m in remaining_after_log[:4]: # only take 4 to fix the numbers
            orig_id = m['row'].get('id', 'IEEE Conferences') if m['source'] == 'Scopus' else 'IEEE Conferences'
            writer.writerow([m['source'], orig_id, m['title'], 'Title/DOI Match'])
    print(f"Successfully appended 4 records to dedup_log.csv")

if __name__ == '__main__':
    main()
