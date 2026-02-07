#!/usr/bin/env python3
"""
FreeAIAPIKey Cost Calculator - EXACT PRICING VERSION

Calculate your exact savings with FreeAIAPIKey.com using real pricing data.

Usage:
    python cost_calculator.py                    # Interactive mode
    python cost_calculator.py --tokens 1000000   # CLI mode
    python cost_calculator.py --all              # Compare all models

Author: FreeAIAPIKey.com
License: MIT
"""

import argparse
from typing import Dict, Tuple, List

# EXACT PRICING DATA (Per 1M tokens) - February 2025
PRICING = {
    "gpt-5": {
        "name": "GPT-5 (OpenAI)",
        "official_input": 1.25,
        "official_output": 10.00,
        "our_input": 0.25,
        "our_output": 2.00,
        "context": "128K",
        "savings": 80.0
    },
    "claude-opus": {
        "name": "Claude Opus 4.5 (Anthropic)",
        "official_input": 5.00,
        "official_output": 25.00,
        "our_input": 1.00,
        "our_output": 5.00,
        "context": "200K",
        "savings": 80.0
    },
    "claude-sonnet": {
        "name": "Claude Sonnet 4.5 (Anthropic)",
        "official_input": 3.00,
        "official_output": 15.00,
        "our_input": 0.60,
        "our_output": 3.00,
        "context": "200K",
        "savings": 80.0
    },
    "gemini": {
        "name": "Gemini 3 (Google)",
        "official_input": 2.00,
        "official_output": 12.00,
        "our_input": 0.40,
        "our_output": 2.50,
        "context": "1M",
        "savings": 79.2
    },
    "deepseek": {
        "name": "DeepSeek V3.2",
        "official_input": 0.50,
        "official_output": 0.90,
        "our_input": 0.20,
        "our_output": 0.30,
        "context": "64K",
        "savings": 63.3
    },
    "kimi": {
        "name": "Kimi K2.5 (Moonshot)",
        "official_input": 0.90,
        "official_output": 3.50,
        "our_input": 0.25,
        "our_output": 1.00,
        "context": "256K",
        "savings": 71.8
    }
}

def format_currency(amount: float) -> str:
    """Format amount as currency string."""
    return f"${amount:,.2f}"

def calculate_costs(
    tokens_per_month: int,
    model: str,
    input_ratio: float = 0.5
) -> Dict:
    """Calculate detailed cost comparison for a given model."""
    
    if model not in PRICING:
        raise ValueError(f"Unknown model: {model}")
    
    data = PRICING[model]
    
    # Calculate input/output split
    input_tokens = tokens_per_month * input_ratio
    output_tokens = tokens_per_month * (1 - input_ratio)
    input_millions = input_tokens / 1_000_000
    output_millions = output_tokens / 1_000_000
    
    # Official costs
    official_input_cost = data["official_input"] * input_millions
    official_output_cost = data["official_output"] * output_millions
    official_total = official_input_cost + official_output_cost
    
    # Our costs
    our_input_cost = data["our_input"] * input_millions
    our_output_cost = data["our_output"] * output_millions
    our_total = our_input_cost + our_output_cost
    
    # Savings
    monthly_savings = official_total - our_total
    annual_savings = monthly_savings * 12
    savings_percentage = ((official_total - our_total) / official_total * 100) if official_total > 0 else 0
    
    return {
        "model_name": data["name"],
        "context": data["context"],
        "tokens_per_month": tokens_per_month,
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
        "official_input_cost": official_input_cost,
        "official_output_cost": official_output_cost,
        "official_total": official_total,
        "our_input_cost": our_input_cost,
        "our_output_cost": our_output_cost,
        "our_total": our_total,
        "monthly_savings": monthly_savings,
        "annual_savings": annual_savings,
        "savings_percentage": savings_percentage,
        "official_input_price": data["official_input"],
        "official_output_price": data["official_output"],
        "our_input_price": data["our_input"],
        "our_output_price": data["our_output"]
    }

def print_detailed_comparison(result: Dict) -> None:
    """Print detailed cost comparison."""
    print("\n" + "=" * 70)
    print(f"💰 COST BREAKDOWN: {result['model_name']}")
    print(f"   Context Window: {result['context']} tokens")
    print("=" * 70)
    
    print(f"\n📊 USAGE (Monthly):")
    print(f"   Total Tokens: {result['tokens_per_month']:,}")
    print(f"   Input Tokens: {result['input_tokens']:,.0f} (50%)")
    print(f"   Output Tokens: {result['output_tokens']:,.0f} (50%)")
    
    print(f"\n🏢 OFFICIAL API COSTS:")
    print(f"   Input: {format_currency(result['official_input_price'])}/1M × {result['input_tokens']/1_000_000:.2f}M = {format_currency(result['official_input_cost'])}")
    print(f"   Output: {format_currency(result['official_output_price'])}/1M × {result['output_tokens']/1_000_000:.2f}M = {format_currency(result['official_output_cost'])}")
    print(f"   Monthly Total: {format_currency(result['official_total'])}")
    print(f"   Annual Total: {format_currency(result['official_total'] * 12)}")
    
    print(f"\n🚀 FREEAIAPIKEY COSTS:")
    print(f"   Input: {format_currency(result['our_input_price'])}/1M × {result['input_tokens']/1_000_000:.2f}M = {format_currency(result['our_input_cost'])}")
    print(f"   Output: {format_currency(result['our_output_price'])}/1M × {result['output_tokens']/1_000_000:.2f}M = {format_currency(result['our_output_cost'])}")
    print(f"   Monthly Total: {format_currency(result['our_total'])}")
    print(f"   Annual Total: {format_currency(result['our_total'] * 12)}")
    
    print(f"\n✅ YOUR SAVINGS:")
    print(f"   Monthly: {format_currency(result['monthly_savings'])}")
    print(f"   Annual: {format_currency(result['annual_savings'])}")
    print(f"   Percentage: {result['savings_percentage']:.1f}%")
    
    print(f"\n🎯 WHAT YOU COULD DO WITH {format_currency(result['annual_savings'])}:")
    if result['annual_savings'] > 1000:
        print(f"   • Extend your startup runway by {result['annual_savings']/500:.0f} months")
        print(f"   • Hire a part-time developer for {result['annual_savings']/20000:.1f} months")
        print(f"   • Pay for {result['annual_savings']/50:.0f} months of server costs")
    else:
        print(f"   • Pay for {result['annual_savings']/20:.0f} months of tools/subscriptions")
        print(f"   • Invest in marketing or design")
        print(f"   • Build more features!")
    
    print("\n" + "=" * 70)
    print("🌐 Get Started: https://freeaiapikey.com | $2 Free Credit")
    print("=" * 70 + "\n")

def print_comparison_table(tokens_per_month: int, input_ratio: float = 0.5) -> None:
    """Print comparison table for all models."""
    print("\n" + "=" * 95)
    print(f"📊 COMPARISON: All Models ({tokens_per_month:,} tokens/month, {input_ratio*100:.0f}% input)")
    print("=" * 95)
    print(f"\n{'Model':<25} {'Official':<12} {'Our Price':<12} {'Monthly':<12} {'Savings':<12} {'% Off':<8}")
    print("-" * 95)
    
    for model_key in PRICING.keys():
        result = calculate_costs(tokens_per_month, model_key, input_ratio)
        print(f"{result['model_name']:<25} "
              f"{format_currency(result['official_total']):<12} "
              f"{format_currency(result['our_total']):<12} "
              f"{format_currency(result['monthly_savings']):<12} "
              f"{format_currency(result['annual_savings']):<12} "
              f"{result['savings_percentage']:.0f}%")
    
    print("-" * 95)
    print("\n🎯 Get Started: https://freeaiapikey.com | $2 Free Credit | No Rate Limits")
    print("=" * 95 + "\n")

def interactive_mode():
    """Run interactive cost calculator."""
    print("\n" + "=" * 70)
    print("🚀 FreeAIAPIKey Cost Calculator")
    print("   Calculate your exact savings with real pricing data")
    print("=" * 70)
    print("\n💡 Our pricing: 80% cheaper than official APIs on average")
    print("💰 $2 free credit on signup - no credit card required\n")
    
    # Display model options
    print("Available Models:")
    for i, (key, data) in enumerate(PRICING.items(), 1):
        print(f"  {i}. {data['name']}")
        print(f"     Official: ${data['official_input']:.2f} in / ${data['official_output']:.2f} out")
        print(f"     Our Price: ${data['our_input']:.2f} in / ${data['our_output']:.2f} out ({data['savings']:.0f}% off)")
        print()
    
    print(f"  {len(PRICING) + 1}. Compare All Models")
    
    # Get user input
    try:
        choice = int(input("Select model (number): "))
        if choice < 1 or choice > len(PRICING) + 1:
            print("❌ Invalid selection. Please try again.")
            return
    except ValueError:
        print("❌ Please enter a valid number.")
        return
    
    # Get token usage
    try:
        tokens_input = input("\nMonthly token usage (e.g., 1000000 for 1M, or 1M): ")
        tokens_input = tokens_input.replace(",", "").replace("M", "000000").replace("K", "000")
        tokens_per_month = int(tokens_input)
    except ValueError:
        print("❌ Please enter a valid number.")
        return
    
    # Get input/output ratio
    try:
        ratio_input = input("Input token percentage (default 50%): ").strip()
        if ratio_input:
            input_ratio = int(ratio_input) / 100
        else:
            input_ratio = 0.5
    except ValueError:
        input_ratio = 0.5
    
    # Calculate and display
    if choice <= len(PRICING):
        model_key = list(PRICING.keys())[choice - 1]
        result = calculate_costs(tokens_per_month, model_key, input_ratio)
        print_detailed_comparison(result)
    else:
        print_comparison_table(tokens_per_month, input_ratio)

def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Calculate exact cost savings with FreeAIAPIKey.com",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python cost_calculator.py                    # Interactive mode
  python cost_calculator.py --tokens 1000000   # 1M tokens with GPT-5 (default)
  python cost_calculator.py -t 500000 -m claude-sonnet  # 500K with Claude
  python cost_calculator.py --all -t 10000000  # Compare all at 10M tokens
  python cost_calculator.py --all --input-ratio 0.3  # 30% input, 70% output
        """
    )
    
    parser.add_argument(
        "-t", "--tokens",
        type=int,
        help="Monthly token usage (default: 1000000)"
    )
    
    parser.add_argument(
        "-m", "--model",
        choices=list(PRICING.keys()),
        default="gpt-5",
        help="Model to calculate for (default: gpt-5)"
    )
    
    parser.add_argument(
        "--all",
        action="store_true",
        help="Compare all available models"
    )
    
    parser.add_argument(
        "--input-ratio",
        type=float,
        default=0.5,
        help="Ratio of input tokens (default: 0.5 = 50%%)"
    )
    
    parser.add_argument(
        "--list",
        action="store_true",
        help="List all models and their pricing"
    )
    
    args = parser.parse_args()
    
    # List models and exit
    if args.list:
        print("\n" + "=" * 80)
        print("📋 Available Models and Pricing (Per 1 Million Tokens)")
        print("=" * 80)
        print(f"\n{'Model':<30} {'Official':<20} {'Our Price':<20} {'Savings':<10}")
        print("-" * 80)
        
        for key, data in PRICING.items():
            official_str = f"${data['official_input']:.2f} / ${data['official_output']:.2f}"
            our_str = f"${data['our_input']:.2f} / ${data['our_output']:.2f}"
            print(f"{data['name']:<30} {official_str:<20} {our_str:<20} {data['savings']:.0f}%")
        
        print("-" * 80)
        print("\n🎯 Get $2 Free: https://freeaiapikey.com")
        print("=" * 80 + "\n")
        return
    
    # If no arguments provided, run interactive mode
    if len([arg for arg in [args.tokens, args.all] if arg]) == 0:
        interactive_mode()
        return
    
    # Use default tokens if not specified
    tokens = args.tokens or 1_000_000
    
    if args.all:
        # Compare all models
        print_comparison_table(tokens, args.input_ratio)
    else:
        # Single model calculation
        result = calculate_costs(tokens, args.model, args.input_ratio)
        print_detailed_comparison(result)

if __name__ == "__main__":
    main()
