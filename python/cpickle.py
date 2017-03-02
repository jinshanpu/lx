import cPickle as p

shopListFile = 'shoplist.data'
shoplist = ['apple', 'mango', 'carrot']

f = file(shopListFile, 'w')
p.dump(shoplist, f)
f.close()

f = file(shopListFile)
storedlist = p.load(f)
print storedlist
