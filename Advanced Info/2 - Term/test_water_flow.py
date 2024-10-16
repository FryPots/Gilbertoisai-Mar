import pytest
import water_flow


def test_water_column_height():
    assert water_flow.water_column_height( 0.0,  0.0) == 0.0
    assert water_flow.water_column_height( 0.0, 10.0) == 7.5
    assert water_flow.water_column_height(25.0,  0.0) == 25.0
    assert water_flow.water_column_height(48.3, 12.8) == 57.9
    
def test_pressure_gain_from_water_hight():
    assert water_flow.pressure_gain_from_water_height( 0.0) == 0.000
    assert water_flow.pressure_gain_from_water_height(30.2) == 295.628
    assert water_flow.pressure_gain_from_water_height(50.0) == 489.450

pytest.main(["-v", "--tb=line", "-rN", __file__])