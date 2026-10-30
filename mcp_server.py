import sys
import json
from client import InfluencerTrackerEngine

def handle_request(req):
    method = req.get("method")
    if method == "tools/list":
        return {
            "tools": [{
                "name": "audit_campaign",
                "description": "Calculate influencer ROAS, conversion rate, and CPM attribution",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "influencer_handle": {"type": "string"},
                        "sponsorship_fee": {"type": "number"},
                        "impressions": {"type": "integer"},
                        "conversions": {"type": "array"}
                    },
                    "required": ["influencer_handle", "sponsorship_fee", "impressions", "conversions"]
                }
            }]
        }
    elif method == "tools/call":
        args = req.get("params", {}).get("arguments", {})
        out = InfluencerTrackerEngine.audit_campaign(
            args.get("influencer_handle", ""),
            float(args.get("sponsorship_fee", 0.0)),
            int(args.get("impressions", 1)),
            args.get("conversions", [])
        )
        return {"content": [{"type": "text", "text": json.dumps(out, indent=2)}]}
    return {"error": "Unsupported method"}

if __name__ == "__main__":
    for line in sys.stdin:
        if not line.strip(): continue
        try:
            req = json.loads(line)
            res = handle_request(req)
            print(json.dumps({"id": req.get("id"), "result": res}))
            sys.stdout.flush()
        except Exception as e:
            print(json.dumps({"error": str(e)}))
            sys.stdout.flush()
