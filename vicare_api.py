import sys
import logging
sys.path.insert(0, 'PyViCare')
from PyViCare.PyViCareDevice import Device
from PyViCare.PyViCareGazBoiler import GazBoiler
from PyViCare.PyViCareService import ViCareService
from PyViCare.PyViCare import ViCareSession
from dane import dane
t=ViCareSession(*dane)


#EXAMPLE: GETTING SETTINGS
print("DomesticHotWaterConfiguredTemperature: ", t.getDomesticHotWaterConfiguredTemperature()) 
print("Outside_Temperature: ", t.getOutsideTemperature())
print("RoomTemperature: ", t.getRoomTemperature())
print("HeatingCurveShift: ", t.getHeatingCurveShift()) 
print("HeatingCurveSlope: ", t.getHeatingCurveSlope()) 
print("ActiveProgram: ", t.getActiveProgram())
print("CurrentDesiredTemperature: ", t.getCurrentDesiredTemperature())
print("DesiredTemperatureForProgram: ", t.getDesiredTemperatureForProgram("comfort"))
print("ActiveMode: ", t.getActiveMode())
print("DesiredTemperatureForProgram: ", t.getDesiredTemperatureForProgram("comfort"))

#EXAMPLE SETTING SETTINGS
print("ProgramTemperature: ", t.setProgramTemperature("comfort",23))
print("DomesticHotWaterTemperature_SET: ", t.setDomesticHotWaterTemperature(40))
print("deactivateProgram: ", t.deactivateComfort())


