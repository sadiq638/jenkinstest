def red(x):
  n=[]
  j=[]
  a=[]
  s=[]
  for i in x:
     if x[i]=='Name':
        n.append(i)
     elif x[i]=='Age':
        a.append(i)
     elif x[i]=='Sex':
        s.append(i)
     elif x[i]=='Job':
        j.append(i)
  d={}
  d['name']=n
  d['age']=a
  d['sex']=s
  d['job']=j
  print(d)

red( {
  "Mubashir": "Name",
  "31": "Age",
  "Male": "Sex",
  "Pilot": "Job",
  "Matt": "Name",
  "40": "Age",
  "Programmer": "Job"
})
