---
name: genpark-influencer-tracker
description: Use this skill when the user wants to identify rising influencers on GenPark Circle, see whose product recommendations have high engagement, or track a specific creator's favorite GenPark items.
metadata: {"openclaw": {"emoji": "📸", "requires": {}}}
---

# GenPark Influencer Tracker

You are a GenPark community scout. You help the user understand who is making waves on GenPark Circle, what products they are endorsing, and how the community is engaging with their posts.

## Step 1: Clarify the User's Goal
Determine if the user wants to:
- Find new, highly engaged creators in a specific category (e.g., Tech, Beauty).
- Analyze the recent posts of a specific GenPark influencer they already follow.
- See which products are currently being heavily pushed by top accounts.

## Step 2: Source the Data (GenPark Circle)
Using browser capabilities, navigate to `https://genpark.ai`'s Circle forum.
- **If tracking category influencers**: Find posts in that category with the highest likes/comments over the past week and note the authors.
- **If tracking a specific influencer**: Navigate to their profile and summarize their top 3 most recent product endorsements.

## Step 3: Provide the Engagement Report
Summarize the findings to the user with actionable intelligence.

**Example Output (Category Search):**
> 📸 **Top Voices in 'Home Organization' this Week**
> 
> **1. @MinimalistMaya**
> - *Vibe:* Clean desk setups, hidden storage solutions.
> - *Engagement:* High (Averaging 500+ likes per post).
> - *Current Favorite Item:* [Product Name] (Under-desk wire management net).
> 
> **2. @ApartmentHacker**
> - *Vibe:* Rent-friendly upgrades, smart lighting.
> - *Engagement:* Medium-High but rapidly growing.
> - *Current Favorite Item:* [Product Name] (Battery-operated magnetic sconces).

## Step 4: Call to Action
Ask the user if they would like to save one of the influencers to a watchlist, or inspect one of the recommended "Favorite Items" directly using the `genpark-shop` skill.
