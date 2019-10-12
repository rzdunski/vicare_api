import sys
import logging
sys.path.insert(0, 'PyViCare')
from PyViCare.PyViCareDevice import Device
from PyViCare.PyViCareGazBoiler import GazBoiler
from PyViCare.PyViCareService import ViCareService
from PyViCare.PyViCare import ViCareSession
from dane import dane
t=ViCareSession(*dane)

print("DomesticHotWaterConfiguredTemperature: ", t.getDomesticHotWaterConfiguredTemperature()) 

print("Outside_Temperature: ", t.getOutsideTemperature())
print("RoomTemperature: ", t.getRoomTemperature())
#print("Supply_Temperature: ", t.getSupplyTemperature())
print("HeatingCurveShift: ", t.getHeatingCurveShift()) 
print("HeatingCurveSlope: ", t.getHeatingCurveSlope()) 
#print("BoilerTemperature:", t.getBoilerTemperature())
print("ActiveProgram: ", t.getActiveProgram())

# print("Programs: ", t.getPrograms())

print("CurrentDesiredTemperature: ", t.getCurrentDesiredTemperature())
#print("MonthSinceLastService: ", t.getMonthSinceLastService())
#print("LastServiceDate: ", t.getLastServiceDate())

print("DesiredTemperatureForProgram: ", t.getDesiredTemperatureForProgram("comfort"))
print("ActiveMode: ", t.getActiveMode())

print("DesiredTemperatureForProgram: ", t.getDesiredTemperatureForProgram("comfort"))
print("ProgramTemperature: ", t.setProgramTemperature("comfort",23))
#print("activateProgram after set: ", t.activateProgram("comfort"))
print("DomesticHotWaterTemperature_SET: ", t.setDomesticHotWaterTemperature(40))
#print("activateProgram: ", t.activateProgram("comfort"))
print("deactivateProgram: ", t.deactivateComfort())
print("CurrentPower: ", t.getCurrentPower())
print(t.getCirculationPumpActive())
print(t.getBurnerModulation())
print(t.getGasConsumptionHeatingYears())
print("GasConsumptionHeatingThisMonth: ", t.getGasConsumptionHeatingThisMonth())
print(t.getGasConsumption())


