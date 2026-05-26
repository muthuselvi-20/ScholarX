import pandas as pd

def validation(df):
    error = []
    # Check for null values
    if df.isnull().sum().sum() > 0:
        error.append("DataFrame contains null values")

    # Check for invalid age values (assuming age should be between 0 and 120)   
    if (df["age"] < 0).any() or (df["age"] > 120).any():
        error.append("DataFrame contains invalid age values")

    valid_gender = [0,1]
    if not df["gender"].isin(valid_gender).all():
        error.append("DataFrame contains invalid gender values")

    # Check for invalid social interaction level values (assuming it should be between 0 and 24)
    if (df["daily_social_media_hours"] < 0).any() or (df["daily_social_media_hours"] > 24).any():
        error.append("DataFrame contains invalid daily social media hours values")

    # Check for invalid platform usage values (assuming it should be between 0 and 2)
    valid_platform_usage = [0, 1, 2]
    if not df["platform_usage"].isin(valid_platform_usage).all():
        error.append("DataFrame contains invalid platform usage values")
    
    # Check for invalid sleep hours values (assuming it should be between 0 and 24) 
    if (df["sleep_hours"] < 0).any() or (df["sleep_hours"] > 24).any():
        error.append("DataFrame contains invalid sleep hours values")

    # Check for invalid screen time before sleep values (assuming it should be between 0 and 24)
    if (df["screen_time_before_sleep"] < 0).any() or (df["screen_time_before_sleep"] > 24).any():
        error.append("DataFrame contains invalid screen time before sleep values")

    # Check for invalid values in academic performance, physical activity, social interaction level, stress level, anxiety level, and addiction level (assuming they should be between 0 and 10)
    for col in ["academic_performance","physical_activity","social_interaction_level","stress_level","anxiety_level","addiction_level"]:
        if (df[col]<0).any() or (df[col]>10).any():
            error.append(f"DataFrame contains invalid {col} values")

    return error

