import numpy as np
from common import *

def run():
    r=rng(71);x=r.normal(size=(250,6));y=x@np.array([1,2,-1,.5,0,1])+r.normal(0,.3,len(x));x[0]*=8;y[0]+=10
    penalty=.1
    def train(z,t):return np.linalg.solve(z.T@z+penalty*np.eye(z.shape[1]),z.T@t)
    original=train(x,y);retained=train(x[1:],y[1:])
    # One gradient-ascent removal step; deliberately approximate, compare full retrain.
    approximate=original+.002*x[0]*(x[0]@original-y[0])
    test=r.normal(size=(100,6));truth=test@np.array([1,2,-1,.5,0,1])
    result={}
    for name,w in [('original',original),('full_retrain',retained),('approximate_update',approximate)]:
        result[name]={'test_rmse':float(np.sqrt(np.mean((test@w-truth)**2))),
                      'removed_record_residual':float(abs(x[0]@w-y[0])),
                      'distance_from_retrain':float(np.linalg.norm(w-retained))}
    result.update(checks=[check(not np.allclose(original,retained),'Removal changes fitted parameters'),check(np.isfinite(approximate).all(),'Finite approximate update')],
                  scope='Ridge-regression removal experiment. Parameter agreement and utility are not proof of forgetting or privacy.')
    return result
