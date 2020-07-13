def determine_elem(libfqn):
    ''' Uses the lib_fqn JSON entry to return the element type '''

    elem_dict = {
        "Sources.Independent Sources.Voltage.AC Voltage Source":"Vac",
        "Sources.Independent Sources.Voltage.DC Voltage Source":"Vdc",
        "Sources.Independent Sources.Voltage.Pulse Voltage Source":"Vpulse",
        "Sources.Independent Sources.Voltage.Exponent Voltage Source":"Vexp",
        "Sources.Independent Sources.Voltage.Triangular Voltage Source":"Vtri",
        "Sources.Independent Sources.Current.AC Current Source":"Iac",
        "Sources.Independent Sources.Current.DC Current Source":"Idc",
        "Sources.Independent Sources.Current.Pulse Current Source":"Ipulse",
        "Sources.Independent Sources.Current.Exponent Current Source":"Iexp",
        "Sources.Controlled Sources.Voltage-Controlled Voltage Source":"VCVS",
        "Sources.Controlled Sources.Voltage-Controlled Current Source":"VCCS",
        "Sources.Controlled Sources.Current-Controlled Voltage Source":"CCVS",
        "Sources.Controlled Sources.Current-Controlled Current Source":"CCCS",
        "Sources.Ground":"GND",
        "Electronics.Operational Amplifier":"OPAMP",
        "Electronics.Ideal Comparator":"COMP",
        "Electronics.Pulse Width Modulator":"PWM",
        "Measurements.Current Measurement":"I_meas",
        "Measurements.Voltage Measurement":"V_meas",
        "Passive Elements.Ideal Resistor":"R",
        "Passive Elements.Ideal Capacitor":"C",
        "Passive Elements.Ideal Inductor":"L",
        "Passive Elements.Transformer":"Transf",
        "Passive Elements.Coupled Inductor":"L_coupled",
        "Passive Elements.Memristor":"ymemristor",
        "SubcircuitElement.3PResistor":"3PResistor", ## Ficticious
        "Sources.Three Phase Voltage Source":"3PVoltageSource",
        "Switches.Diode":"D",
        "Switches.Ideal Diode":"IdealD",
        "Switches.Unidirectional Switch":"UnidirSwitch",
        "Switches.MOSFET":"M",
        "Switches.JFET":"J",
        "Switches.BJT":"Q",
        "Switches.MESFET":"Z",
        "Switches.Voltage-Controlled Switch":"S",
        "Switches.Current-Controlled Switch":"W",
        "Transmission Lines.Ideal Transmission Line":"T",
        "Transmission Lines.Lossy Transmission Line":"O",
        "Transmission Lines.Lumped Transmission sLine":"ytransline",
        "Behavioral Digital.Inverter":"U",
        "Behavioral Digital.AND":"U",
        "Behavioral Digital.OR":"U",
        "Behavioral Digital.Delay_":"U",
        "Special.Dynamic SPICE component":"Smart",
        "Special.NodeID":"NodeID",
    }

    if libfqn in elem_dict.keys():
        return elem_dict[libfqn]
