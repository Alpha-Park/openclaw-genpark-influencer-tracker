from client import InfluencerTrackerEngine

if __name__ == "__main__":
    res = InfluencerTrackerEngine.audit_campaign(
        "@tech_creator", 1200.0, 50000,
        [{"order_value": 75.0}, {"order_value": 120.0}, {"order_value": 2400.0}]
    )
    print("Campaign Audit:", res)
