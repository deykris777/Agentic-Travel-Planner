from data.city_cost_data import get_base_cost

STYLE_MULTIPLIER = {
    "Budget": 0.8,
    "Balanced": 1.0,
    "Luxury": 1.5
}

def analyze_trip(country, city, days, budget, style):
    base = get_base_cost(country)

    multiplier = STYLE_MULTIPLIER.get(style, 1.0)

    daily_cost = int(base["daily"] * multiplier)
    stay_cost = daily_cost * days
    flight_cost = base["flight"]
    buffer = int(0.1 * stay_cost)

    total_cost = stay_cost + flight_cost + buffer

    explanation = []

    if budget >= total_cost:
        verdict = "Affordable"
        confidence = "High"
        explanation.append("Budget comfortably covers all estimated expenses.")
    elif budget >= total_cost * 0.75:
        verdict = "Tight Budget"
        confidence = "Medium"
        explanation.append("Trip is possible but with limited flexibility.")
    else:
        verdict = "Not Feasible"
        confidence = "Low"
        explanation.append("Budget is insufficient for this destination and duration.")

    if days > 10:
        explanation.append("Longer trip duration significantly increases total cost.")

    if style == "Luxury":
        explanation.append("Luxury travel style increases accommodation and lifestyle expenses.")

    return {
        "daily_cost": daily_cost,
        "stay_cost": stay_cost,
        "flight_cost": flight_cost,
        "buffer": buffer,
        "total_cost": total_cost,
        "confidence": confidence,
        "verdict": verdict,
        "explanation": explanation
    }
