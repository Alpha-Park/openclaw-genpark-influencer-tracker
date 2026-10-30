"""Influencer Campaign ROI & Conversion Tracker.
100% Python Standard Library.
"""

class InfluencerTrackerEngine:
    """Benchmarks influencer conversion rates, net revenue attribution, and effective ROAS."""

    @staticmethod
    def audit_campaign(influencer_handle: str, sponsorship_fee: float, impressions: int, conversions: list) -> dict:
        total_attributed_revenue = sum(float(c.get("order_value", 0.0)) for c in conversions)
        conversions_count = len(conversions)

        roas = (total_attributed_revenue / max(1.0, sponsorship_fee))
        conversion_rate = (conversions_count / max(1, impressions)) * 100.0
        cpm = (sponsorship_fee / max(1, impressions)) * 1000.0

        return {
            "influencer": influencer_handle,
            "sponsorship_fee": round(sponsorship_fee, 2),
            "impressions": impressions,
            "conversions_count": conversions_count,
            "total_attributed_revenue": round(total_attributed_revenue, 2),
            "roas": round(roas, 2),
            "cpm": round(cpm, 2),
            "conversion_rate_pct": round(conversion_rate, 4),
            "performance_verdict": "PROFITABLE" if roas >= 2.0 else "UNDERPERFORMING"
        }
