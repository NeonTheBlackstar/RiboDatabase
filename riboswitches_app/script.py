from database.models import RiboFamily, RiboClass


'''
for i in RiboClass.objects.all():
	i.delete()

for i in RiboFamily.objects.all():
	i.delete()


c = RiboClass(name = 'NazwaC', description = 'OpisC', alignment = 'AlajC')
c.save()
f = RiboFamily(ribo_class = c, name = 'NazwaF', description = 'OpisF', alignment = 'AlajF')
f.save()

c = RiboClass(name = 'NazwaC2', description = 'OpisC2', alignment = 'AlajC2')
c.save()
f = RiboFamily(ribo_class = c, name = 'NazwaF2', description = 'OpisF2', alignment = 'AlajF2')
f.save()
'''


print(RiboFamily.objects.all())
print(RiboClass.objects.all())
c = RiboClass.objects.all()[0]
print(c.ribofamily_set.all())
