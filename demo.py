"""A small data analysis example."""

import pandas as pd


def main():
    data = pd.DataFrame({"item": ["A", "B", "C"], "value": [10, 20, 30]})
    print(data.to_string(index=False))
    print(f"Average: {data['value'].mean():.1f}")


if __name__ == "__main__":
    main()
