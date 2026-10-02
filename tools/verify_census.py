import csv
import os
import pandas as pd

def count_rows(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8-sig') as f:
            reader = csv.reader(f)
            headers = next(reader, None)
            return sum(1 for row in reader)
    except Exception as e:
        return f"Error: {e}"

def main():
    print("=" * 60)
    print("      PRISMA 2020 PIPELINE CENSUS VERIFICATION")
    print("=" * 60)
    
    # 1. Raw Data (2000 total: 1000 IEEE + 1000 Scopus)
    ieee_path = os.path.join('01_data', '01_data_raw', 'ieee_xplore_20260615.csv')
    scopus_path = os.path.join('01_data', '01_data_raw', 'scopus_20260615.csv')
    ieee_count = count_rows(ieee_path)
    scopus_count = count_rows(scopus_path)
    print(f"\n1. Raw Data:")
    print(f"  - IEEE Xplore: {ieee_count} (Expected: 1000)")
    print(f"  - Scopus:      {scopus_count} (Expected: 1000)")
    print(f"  - Total Raw:   {ieee_count + scopus_count} (Expected: 2000)")
    
    # 2. Deduplication (1716 retained, 284 duplicate records logged)
    dedup_master = os.path.join('01_data', '02_data_proceesed', '01_deduplicated_master.csv')
    dedup_log = os.path.join('01_data', '02_data_proceesed', 'dedup_log.csv')
    dedup_master_count = count_rows(dedup_master)
    dedup_log_count = count_rows(dedup_log)
    print(f"\n2. Deduplication:")
    print(f"  - Deduplicated Master: {dedup_master_count} (Expected: 1716)")
    print(f"  - Dedup Log:           {dedup_log_count} (Expected: 284)")
    
    # 3. Screening (501 screened candidates)
    screened_inc = os.path.join('01_data', '02_data_proceesed', '02_screened_included_v2.csv')
    screened_inc_count = count_rows(screened_inc)
    print(f"\n3. Title & Abstract Screening:")
    print(f"  - Candidate Pool:      {screened_inc_count} (Expected: 501)")
    
    # 4. Full-Text Assessment & Retrieval (291 total)
    screening_res = os.path.join('01_data', '02_data_proceesed', '03_screening_results.csv')
    retrieved_csv = os.path.join('01_data', '02_data_proceesed', '04_retrieved_pdfs_291.csv')
    df_scr = pd.read_csv(screening_res)
    inc_count = len(df_scr[df_scr['decision'] == 'INCLUDE'])
    exc_count = len(df_scr[df_scr['decision'] != 'INCLUDE'])
    e1_count = len(df_scr[df_scr['rule'] == 'E1'])
    e3_count = len(df_scr[df_scr['rule'] == 'E3'])
    
    print(f"\n4. Full-Text Assessment & Eligibility:")
    print(f"  - Total Assessed:      {len(df_scr)} (Expected: 291)")
    print(f"  - Total Retrieved CSV: {count_rows(retrieved_csv)} (Expected: 291)")
    print(f"  - Included Studies:    {inc_count} (Expected: 287)")
    print(f"  - Excluded Studies:    {exc_count} (Expected: 4)")
    print(f"    * E1 (Scope):        {e1_count} (REC_0053, REC_0693, REC_0866)")
    print(f"    * E3 (Language):     {e3_count} (REC_1688, Chinese full text)")
    
    # 5. Disk File Parity (PDFs, Cards, Manifest)
    pdf_dir = os.path.join('01_data', '03_pdfs')
    pdf_count = len([f for f in os.listdir(pdf_dir) if f.endswith('.pdf')])
    card_dir = '02_cards'
    card_count = len([f for f in os.listdir(card_dir) if f.startswith('REC_') and f.endswith('.md')])
    manifest_count = count_rows(os.path.join(card_dir, 'FROZEN_MANIFEST_20260927.csv'))
    
    print(f"\n5. Physical Asset Parity on Disk:")
    print(f"  - PDFs in 01_data/03_pdfs/: {pdf_count} (Expected: 291)")
    print(f"  - Evidence Cards (02_cards): {card_count} (Expected: 291)")
    print(f"  - Card Manifest Rows:        {manifest_count} (Expected: 291)")
    
    # Overall Status Check
    all_ok = (
        ieee_count == 1000 and scopus_count == 1000 and
        dedup_master_count == 1716 and dedup_log_count == 284 and
        screened_inc_count == 501 and len(df_scr) == 291 and
        inc_count == 287 and exc_count == 4 and
        pdf_count == 291 and card_count == 291 and manifest_count == 291
    )
    print("\n" + "=" * 60)
    print(f"AUDIT VERIFICATION RESULT: {'PASSED (100% Census Alignment)' if all_ok else 'FAILED'}")
    print("=" * 60)

if __name__ == '__main__':
    main()
