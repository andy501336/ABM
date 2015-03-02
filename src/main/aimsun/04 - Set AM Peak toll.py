sectionType = model.getType("GKSection")
amTollAtt = model.getColumn("GKSection::ITOLLA")
for section in model.getCatalog().getObjectsByType(sectionType).itervalues():
	toll = float(section.getDataValueInt(amTollAtt))/100
	section.setUserDefinedCost(toll)
print "Done!"