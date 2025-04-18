# automatically generated by the FlatBuffers compiler, do not modify

# namespace: 

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class TSData(object):
    __slots__ = ['_tab']

    @classmethod
    def SizeOf(cls):
        return 96

    # TSData
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # TSData
    def IsEmergency(self): return self._tab.Get(flatbuffers.number_types.BoolFlags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(0))
    # TSData
    def IsEmergencyButtonPressed(self): return self._tab.Get(flatbuffers.number_types.BoolFlags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(1))
    # TSData
    def IsEmergencySwitchToggled(self): return self._tab.Get(flatbuffers.number_types.BoolFlags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(2))
    # TSData
    def IsHydrogenLeaking(self): return self._tab.Get(flatbuffers.number_types.BoolFlags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(3))
    # TSData
    def IsScRelayClosed(self): return self._tab.Get(flatbuffers.number_types.BoolFlags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(4))
    # TSData
    def IsTimeResetButtonPressed(self): return self._tab.Get(flatbuffers.number_types.BoolFlags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(5))
    # TSData
    def IsHalfSpeedButtonPressed(self): return self._tab.Get(flatbuffers.number_types.BoolFlags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(6))
    # TSData
    def IsGasButtonPressed(self): return self._tab.Get(flatbuffers.number_types.BoolFlags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(7))
    # TSData
    def FuelCellMode(self): return self._tab.Get(flatbuffers.number_types.Int8Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(8))
    # TSData
    def FcCurrent(self): return self._tab.Get(flatbuffers.number_types.Float32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(12))
    # TSData
    def FcScCurrent(self): return self._tab.Get(flatbuffers.number_types.Float32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(16))
    # TSData
    def ScMotorCurrent(self): return self._tab.Get(flatbuffers.number_types.Float32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(20))
    # TSData
    def FcVoltage(self): return self._tab.Get(flatbuffers.number_types.Float32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(24))
    # TSData
    def ScVoltage(self): return self._tab.Get(flatbuffers.number_types.Float32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(28))
    # TSData
    def HydrogenSensorVoltage(self): return self._tab.Get(flatbuffers.number_types.Float32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(32))
    # TSData
    def FuelCellTemperature(self): return self._tab.Get(flatbuffers.number_types.Float32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(36))
    # TSData
    def FanRpm(self): return self._tab.Get(flatbuffers.number_types.Int32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(40))
    # TSData
    def VehicleSpeed(self): return self._tab.Get(flatbuffers.number_types.Float32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(44))
    # TSData
    def MotorPwm(self): return self._tab.Get(flatbuffers.number_types.Int32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(48))
    # TSData
    def HydrogenPressure(self): return self._tab.Get(flatbuffers.number_types.Float32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(52))
    # TSData
    def GpsLatitude(self): return self._tab.Get(flatbuffers.number_types.Float32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(56))
    # TSData
    def GpsLongitude(self): return self._tab.Get(flatbuffers.number_types.Float32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(60))
    # TSData
    def GpsAltitude(self): return self._tab.Get(flatbuffers.number_types.Float32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(64))
    # TSData
    def GpsSpeed(self): return self._tab.Get(flatbuffers.number_types.Float32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(68))
    # TSData
    def MotorSpeed(self): return self._tab.Get(flatbuffers.number_types.Float32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(72))
    # TSData
    def MotorCurrent(self): return self._tab.Get(flatbuffers.number_types.Float32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(76))
    # TSData
    def FcCurrentRaw(self): return self._tab.Get(flatbuffers.number_types.Float32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(80))
    # TSData
    def FcVoltageRaw(self): return self._tab.Get(flatbuffers.number_types.Float32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(84))
    # TSData
    def McCurrent(self): return self._tab.Get(flatbuffers.number_types.Float32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(88))
    # TSData
    def LapNumber(self): return self._tab.Get(flatbuffers.number_types.Uint8Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(92))

def CreateTSData(builder, isEmergency, isEmergencyButtonPressed, isEmergencySwitchToggled, isHydrogenLeaking, isScRelayClosed, isTimeResetButtonPressed, isHalfSpeedButtonPressed, isGasButtonPressed, fuelCellMode, fcCurrent, fcScCurrent, scMotorCurrent, fcVoltage, scVoltage, hydrogenSensorVoltage, fuelCellTemperature, fanRpm, vehicleSpeed, motorPwm, hydrogenPressure, gpsLatitude, gpsLongitude, gpsAltitude, gpsSpeed, motorSpeed, motorCurrent, fcCurrentRaw, fcVoltageRaw, mcCurrent, lapNumber):
    builder.Prep(4, 96)
    builder.Pad(3)
    builder.PrependUint8(lapNumber)
    builder.PrependFloat32(mcCurrent)
    builder.PrependFloat32(fcVoltageRaw)
    builder.PrependFloat32(fcCurrentRaw)
    builder.PrependFloat32(motorCurrent)
    builder.PrependFloat32(motorSpeed)
    builder.PrependFloat32(gpsSpeed)
    builder.PrependFloat32(gpsAltitude)
    builder.PrependFloat32(gpsLongitude)
    builder.PrependFloat32(gpsLatitude)
    builder.PrependFloat32(hydrogenPressure)
    builder.PrependInt32(motorPwm)
    builder.PrependFloat32(vehicleSpeed)
    builder.PrependInt32(fanRpm)
    builder.PrependFloat32(fuelCellTemperature)
    builder.PrependFloat32(hydrogenSensorVoltage)
    builder.PrependFloat32(scVoltage)
    builder.PrependFloat32(fcVoltage)
    builder.PrependFloat32(scMotorCurrent)
    builder.PrependFloat32(fcScCurrent)
    builder.PrependFloat32(fcCurrent)
    builder.Pad(3)
    builder.PrependInt8(fuelCellMode)
    builder.PrependBool(isGasButtonPressed)
    builder.PrependBool(isHalfSpeedButtonPressed)
    builder.PrependBool(isTimeResetButtonPressed)
    builder.PrependBool(isScRelayClosed)
    builder.PrependBool(isHydrogenLeaking)
    builder.PrependBool(isEmergencySwitchToggled)
    builder.PrependBool(isEmergencyButtonPressed)
    builder.PrependBool(isEmergency)
    return builder.Offset()
