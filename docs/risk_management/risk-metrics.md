# Risk Metrics

## Volatility (Standard Deviation)
Volatility measures how much an investment's returns fluctuate over time, usually expressed as standard deviation. A higher standard deviation means larger price swings in both directions. Volatility is not the same as loss — a volatile asset can still trend upward over the long run, but the ride will feel bumpier.

## Beta
Beta measures how a stock or portfolio moves relative to the overall market, typically benchmarked against an index like the S&P 500. A beta of 1.0 means the asset tends to move in line with the market. A beta above 1.0 means the asset is more volatile than the market, and a beta below 1.0 means it is less volatile.

## Sharpe Ratio
The Sharpe ratio measures risk-adjusted return: how much return an investment generates per unit of risk taken. It is calculated as the portfolio's return minus the risk-free rate, divided by the portfolio's standard deviation. A higher Sharpe ratio indicates a more efficient portfolio, generating more return for the same amount of risk.

## Maximum Drawdown
Maximum drawdown is the largest peak-to-trough decline an investment or portfolio has experienced over a given period. It is a useful way to communicate real-world downside risk to a user, since "your portfolio could have dropped 35% during the worst period" is more intuitive than a standard deviation figure.

## Diversifiable vs Non-Diversifiable Risk
Diversifiable (unsystematic) risk is specific to a single company or sector, such as a product recall or a lawsuit, and can be reduced by holding a broad mix of investments. Non-diversifiable (systematic) risk affects the entire market, such as a recession or interest rate change, and cannot be eliminated through diversification alone.

## Using Risk Metrics in Recommendations
When Finvest AI discusses risk with a user, it should translate these metrics into plain language tied to the user's own risk profile rather than presenting raw numbers without context. For example, explaining what a given maximum drawdown would have meant in dollar terms for their actual portfolio size is more useful than citing standard deviation alone.
