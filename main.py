import ast
import inspect
from rule_engine import RuleEngine

# Kullanıcı verisi
users = [
    {"age": 25, "membership": "gold", "region": "EU", "base_price": 100},
    {"age": 17, "membership": "gold", "region": "US", "base_price": 120},
    {"age": 30, "membership": "silver", "region": "EU", "base_price": 80},
    {"age": 22, "membership": "silver", "region": "US", "base_price": 90},
    {"age": 16, "membership": "gold", "region": "EU", "base_price": 150},
    {"age": 45, "membership": "platinum", "region": "EU", "base_price": 200},
    {"age": 19, "membership": "silver", "region": "EU", "base_price": 75},
    {"age": 50, "membership": "gold", "region": "US", "base_price": 180},
    {"age": 12, "membership": "silver", "region": "US", "base_price": 50},
    {"age": 28, "membership": "bronze", "region": "EU", "base_price": 60},
]


def calculate_discount_branching(user):
    """
    Branching yöntemi ile indirim ve mesaj hesaplama
    """
    if user["membership"] == "gold":
        if user["age"] > 18:
            message = f"{user['membership'].title()} adult member"
            final_price = user["base_price"] * 0.80  # %20 indirim
        else:
            message = f"{user['membership'].title()} young member"
            final_price = user["base_price"] * 0.85  # %15 indirim
    elif user["membership"] == "silver":
        if user["region"] == "EU":
            message = f"{user['membership'].title()} EU member"
            final_price = user["base_price"] * 0.95  # %5 indirim
        else:
            message = "Regular member"
            final_price = user["base_price"]
    else:
        message = "Regular member"
        final_price = user["base_price"]
    
    return {
        "message": message,
        "final_price": final_price
    }


def calculate_discount_rule_engine(user, engine):
    """
    Rule Engine ile indirim ve mesaj hesaplama
    """
    return engine.run(user)


def setup_rule_engine():
    """
    Rule Engine'i kurallarla birlikte hazırla
    """
    engine = RuleEngine()
    
    # Kurallar ve aksiyonlar
    engine.add_rule(
        lambda u: u["membership"] == "gold" and u["age"] > 18,
        lambda u: {
            "message": f"{u['membership'].title()} adult member",
            "final_price": u["base_price"] * 0.80  # %20 indirim
        }
    )
    engine.add_rule(
        lambda u: u["membership"] == "gold" and u["age"] <= 18,
        lambda u: {
            "message": f"{u['membership'].title()} young member",
            "final_price": u["base_price"] * 0.85  # %15 indirim
        }
    )
    engine.add_rule(
        lambda u: u["membership"] == "silver" and u["region"] == "EU",
        lambda u: {
            "message": f"{u['membership'].title()} EU member",
            "final_price": u["base_price"] * 0.95  # %5 indirim
        }
    )
    engine.add_rule(
        lambda u: True,  # default
        lambda u: {
            "message": "Regular member",
            "final_price": u["base_price"]  # indirim yok
        }
    )
    
    return engine


class ComplexityAnalyzer(ast.NodeVisitor):
    """
    Cyclomatic ve Cognitive Complexity hesaplayan sınıf
    """
    
    def __init__(self):
        self.cyclomatic_complexity = 1  # Base complexity
        self.cognitive_complexity = 0
        self.nesting_level = 0
        
    def visit_If(self, node):
        """if/elif/else yapıları için complexity hesaplama"""
        self.cyclomatic_complexity += 1
        self.cognitive_complexity += 1 + self.nesting_level
        self.nesting_level += 1
        self.generic_visit(node)
        self.nesting_level -= 1
        
    def visit_For(self, node):
        """for döngüleri için complexity hesaplama"""
        self.cyclomatic_complexity += 1
        self.cognitive_complexity += 1 + self.nesting_level
        self.nesting_level += 1
        self.generic_visit(node)
        self.nesting_level -= 1
        
    def visit_While(self, node):
        """while döngüleri için complexity hesaplama"""
        self.cyclomatic_complexity += 1
        self.cognitive_complexity += 1 + self.nesting_level
        self.nesting_level += 1
        self.generic_visit(node)
        self.nesting_level -= 1
        
    def visit_ExceptHandler(self, node):
        """try/except yapıları için complexity hesaplama"""
        self.cyclomatic_complexity += 1
        self.cognitive_complexity += 1 + self.nesting_level
        self.nesting_level += 1
        self.generic_visit(node)
        self.nesting_level -= 1
        
    def visit_BoolOp(self, node):
        """and/or operatörleri için complexity hesaplama"""
        if isinstance(node.op, ast.And):
            self.cognitive_complexity += 1
        elif isinstance(node.op, ast.Or):
            self.cognitive_complexity += 1
        self.generic_visit(node)


def calculate_complexity(func):
    """
    Bir fonksiyonun Cyclomatic ve Cognitive Complexity'sini hesaplar
    """
    try:
        source = inspect.getsource(func)
        tree = ast.parse(source)
        
        analyzer = ComplexityAnalyzer()
        analyzer.visit(tree)
        
        return {
            "cyclomatic_complexity": analyzer.cyclomatic_complexity,
            "cognitive_complexity": analyzer.cognitive_complexity,
            "function_name": func.__name__
        }
    except Exception as e:
        return {
            "cyclomatic_complexity": 0,
            "cognitive_complexity": 0,
            "function_name": func.__name__,
            "error": str(e)
        }


def analyze_rule_engine_complexity():
    """
    Rule Engine'in complexity'sini analiz eder
    """
    # Rule Engine sınıfının complexity'si
    engine_complexity = calculate_complexity(RuleEngine.run)
    
    # Kuralların complexity'si (lambda fonksiyonları için manuel hesaplama)
    rules_complexity = {
        "cyclomatic_complexity": 4,  # 4 farklı kural koşulu
        "cognitive_complexity": 6,   # İç içe geçmiş koşullar
        "function_name": "Rule Engine Rules"
    }
    
    return {
        "engine_method": engine_complexity,
        "rules": rules_complexity,
        "total_cyclomatic": engine_complexity["cyclomatic_complexity"] + rules_complexity["cyclomatic_complexity"],
        "total_cognitive": engine_complexity["cognitive_complexity"] + rules_complexity["cognitive_complexity"]
    }


def compare_complexity():
    """
    Branching ve Rule Engine metodlarının complexity'sini karşılaştırır
    """
    print("=" * 70)
    print("COMPLEXITY KARŞILAŞTIRMASI")
    print("=" * 70)
    
    # Branching metodunun complexity'sini hesapla
    print("\n1. BRANCHING YÖNTEMİ COMPLEXITY ANALİZİ:")
    print("-" * 50)
    branching_complexity = calculate_complexity(calculate_discount_branching)
    print(f"   Fonksiyon: {branching_complexity['function_name']}")
    print(f"   Cyclomatic Complexity: {branching_complexity['cyclomatic_complexity']}")
    print(f"   Cognitive Complexity: {branching_complexity['cognitive_complexity']}")
    
    # Rule Engine metodunun complexity'sini hesapla
    print("\n2. RULE ENGINE YÖNTEMİ COMPLEXITY ANALİZİ:")
    print("-" * 50)
    rule_engine_complexity = analyze_rule_engine_complexity()
    
    print(f"   Engine Method:")
    print(f"     Cyclomatic Complexity: {rule_engine_complexity['engine_method']['cyclomatic_complexity']}")
    print(f"     Cognitive Complexity: {rule_engine_complexity['engine_method']['cognitive_complexity']}")
    
    print(f"   Rules:")
    print(f"     Cyclomatic Complexity: {rule_engine_complexity['rules']['cyclomatic_complexity']}")
    print(f"     Cognitive Complexity: {rule_engine_complexity['rules']['cognitive_complexity']}")
    
    print(f"   Toplam:")
    print(f"     Cyclomatic Complexity: {rule_engine_complexity['total_cyclomatic']}")
    print(f"     Cognitive Complexity: {rule_engine_complexity['total_cognitive']}")
    
    # Karşılaştırma
    print("\n3. COMPLEXITY KARŞILAŞTIRMASI:")
    print("-" * 50)
    
    # Cyclomatic Complexity karşılaştırması
    if branching_complexity['cyclomatic_complexity'] < rule_engine_complexity['total_cyclomatic']:
        simpler_cyclomatic = "Branching"
        more_complex_cyclomatic = "Rule Engine"
        cyclomatic_diff = rule_engine_complexity['total_cyclomatic'] - branching_complexity['cyclomatic_complexity']
    else:
        simpler_cyclomatic = "Rule Engine"
        more_complex_cyclomatic = "Branching"
        cyclomatic_diff = branching_complexity['cyclomatic_complexity'] - rule_engine_complexity['total_cyclomatic']
    
    # Cognitive Complexity karşılaştırması
    if branching_complexity['cognitive_complexity'] < rule_engine_complexity['total_cognitive']:
        simpler_cognitive = "Branching"
        more_complex_cognitive = "Rule Engine"
        cognitive_diff = rule_engine_complexity['total_cognitive'] - branching_complexity['cognitive_complexity']
    else:
        simpler_cognitive = "Rule Engine"
        more_complex_cognitive = "Branching"
        cognitive_diff = branching_complexity['cognitive_complexity'] - rule_engine_complexity['total_cognitive']
    
    print(f"   Cyclomatic Complexity:")
    print(f"     Daha basit: {simpler_cyclomatic}")
    print(f"     Fark: {cyclomatic_diff} puan")
    
    print(f"   Cognitive Complexity:")
    print(f"     Daha basit: {simpler_cognitive}")
    print(f"     Fark: {cognitive_diff} puan")
    
    # Genel değerlendirme
    print("\n4. GENEL DEĞERLENDİRME:")
    print("-" * 50)
    
    if (branching_complexity['cyclomatic_complexity'] < rule_engine_complexity['total_cyclomatic'] and 
        branching_complexity['cognitive_complexity'] < rule_engine_complexity['total_cognitive']):
        print("   ✓ Branching yöntemi her iki complexity metrikinde de daha basit")
        print("   ✓ Branching yöntemi daha kolay anlaşılır ve bakımı yapılabilir")
    elif (rule_engine_complexity['total_cyclomatic'] < branching_complexity['cyclomatic_complexity'] and 
          rule_engine_complexity['total_cognitive'] < branching_complexity['cognitive_complexity']):
        print("   ✓ Rule Engine yöntemi her iki complexity metrikinde de daha basit")
        print("   ✓ Rule Engine yöntemi daha kolay anlaşılır ve bakımı yapılabilir")
    else:
        print("   ⚠ Karışık sonuçlar - her yöntem farklı metriklerde avantajlı")
        print("   ⚠ Proje gereksinimlerine göre karar verilmelidir")
    
    return {
        "branching": branching_complexity,
        "rule_engine": rule_engine_complexity
    }


def demonstrate_both_methods(users):
    """
    Her iki yöntemi de gösterir ve sonuçları karşılaştırır
    """
    print("=" * 60)
    print("YÖNTEM KARŞILAŞTIRMASI - SONUÇLAR")
    print("=" * 60)
    
    # Rule Engine'i hazırla
    engine = setup_rule_engine()
    
    print("\nBRANCHING YÖNTEMİ SONUÇLARI:")
    print("-" * 40)
    for i, user in enumerate(users, 1):
        result = calculate_discount_branching(user)
        print(f"{i:2d}. User: {user}")
        print(f"    Result -> Message: {result['message']}, Final Price: ${result['final_price']:.2f}")
    
    print("\nRULE ENGINE YÖNTEMİ SONUÇLARI:")
    print("-" * 40)
    for i, user in enumerate(users, 1):
        result = calculate_discount_rule_engine(user, engine)
        print(f"{i:2d}. User: {user}")
        print(f"    Result -> Message: {result['message']}, Final Price: ${result['final_price']:.2f}")
    
    # Sonuçların aynı olup olmadığını kontrol et
    print("\nSONUÇ DOĞRULAMA:")
    print("-" * 40)
    all_results_match = True
    for i, user in enumerate(users, 1):
        branching_result = calculate_discount_branching(user)
        rule_engine_result = calculate_discount_rule_engine(user, engine)
        
        if (branching_result['message'] == rule_engine_result['message'] and 
            abs(branching_result['final_price'] - rule_engine_result['final_price']) < 0.01):
            print(f"{i:2d}. ✓ Sonuçlar eşleşiyor")
        else:
            print(f"{i:2d}. ✗ Sonuçlar farklı!")
            all_results_match = False
    
    if all_results_match:
        print("\n✓ Tüm sonuçlar eşleşiyor! Her iki yöntem de aynı sonucu veriyor.")
    else:
        print("\n✗ Bazı sonuçlar farklı! Yöntemlerde tutarsızlık var.")


if __name__ == "__main__":
    # Her iki yöntemi de göster
    demonstrate_both_methods(users)
    
    # Complexity karşılaştırması yap
    print("\n")
    compare_complexity()
