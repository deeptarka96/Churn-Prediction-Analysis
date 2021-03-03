import pandas as pd
import numpy as np

def clv_calculator(rev, ser_cost, churn, inc_cost = 0, adr = 0.1):
    
    revenue = np.repeat(rev,60)
    s_cost = np.repeat(ser_cost,60)
    incentive_cost = np.repeat(inc_cost,60)
    profit = revenue-s_cost-incentive_cost
    attrition = np.repeat(churn,59)
    attrition = np.insert(attrition,0,0)
    retention = (1.0-attrition).cumprod()
    exp_profit = retention*profit
    
    dis = np.arange(0,60,1)
    
    mdr = ((1+adr)**(1/12))-1
    
    pv = exp_profit/((1+mdr)**dis)
    
    return pv.sum()

