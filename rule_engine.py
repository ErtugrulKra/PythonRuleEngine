 
# Basit Rule Engine framework
class RuleEngine:
    def __init__(self):
        self.rules = []

    def add_rule(self, condition, action):
        """Kural ekle: condition True olursa action çalışır"""
        self.rules.append({"condition": condition, "action": action})

    def run(self, context):
        for rule in self.rules:
            if rule["condition"](context):
                return rule["action"](context)
 