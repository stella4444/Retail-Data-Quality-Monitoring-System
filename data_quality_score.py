total_rows = len(df)

missing_price_pct = (
    df["price"].isna().sum() / total_rows
) * 100

duplicate_pct = (
    df.duplicated(subset=["sku"]).sum()
    / total_rows
) * 100

quality_score = 100 - (
    missing_price_pct +
    duplicate_pct
)

print(f"Quality Score: {quality_score:.2f}")
