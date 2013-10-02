# -*- coding: utf-8 -*- 


from intervalo import *
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def partIntervalo(intervalo, n):
  nInterv    = np.linspace(intervalo.lo,intervalo.hi, n+1)
  listInterv = [Intervalo(nInterv[i],nInterv[i+1]) for i in range(n)]
  return listInterv
  
def plotFIntevalo(listInterv,Fx=None):
  rnd = np.random.uniform(0.,1.,3)
  nlen = len(listInterv)
  if Fx != None:
    listFx=Fx(listInterv)
    plotF = plt.figure(1,figsize=(12,12),dpi=200)
    ax = plotF.add_subplot(111)
    plt.plot(np.linspace(listInterv[0].lo,listInterv[-1].hi,100),Fx(np.linspace(listInterv[0].lo,listInterv[-1].hi,100)),color=(rnd[0],rnd[1],rnd[2]))
    plt.xlabel('$X$')
    plt.ylabel('$F ( X )$')
    #rect=matplotlib.patches.Rectangle((listInterv[0].lo,listFx[0].lo),listInterv[0].width(),listFx[0].width(),color=(rnd[2],rnd[0],rnd[1]),alpha=0.2)
    #ax.add_patch(rect)
    pltrec = [matplotlib.patches.Rectangle((listInterv[i].lo,listFx[i].lo),listInterv[i].width(),listFx[i].width(),color=(rnd[2],rnd[0],rnd[1]),alpha=0.2) for i in range(nlen)]
    recs   = [ax.add_patch(rec) for rec in pltrec]
    plt.ylim(min(listFx).lo,max(listFx).hi)
    ##plt.show()
    return listFx
  
  else:
    plotF = plt.figure(1)
    #plt.Rectangle((,))
    plt.plot(np.linspace(listInterv[0].lo,listInterv[-1].hi,100),np.cos(np.linspace(listInterv[0].lo,listInterv[-1].hi,100)),color=(0,0,0))
    return plotF

def plot_intevalo(a,y=0):
    mins=[]
    maxs=[]
    for i in a:
      y=y+0.05
      col=np.random.uniform(0.0,1.0,[3])
      plt.figure(1)
      plt.hlines(y,i.lo,i.hi,colors=tuple(col),linewidths=1.5)
      plt.vlines(i.lo,y-0.03,y+0.03,colors=tuple(col),linewidths=1.5)
      plt.vlines(i.hi,y-0.03,y+0.03,colors=tuple(col),linewidths=1.5)
      mins.append(i.lo)
      maxs.append(i.hi)
      
    plt.xlim(min(mins)-1.0,max(maxs)+1.0)
    #plt.ylim(y-0.5,y+0.5)
    return plt.show()