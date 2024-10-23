import pytest
import water_flow


def test_water_column_height():
    assert water_flow.water_column_height( 0.0,  0.0) == 0.0
    assert water_flow.water_column_height( 0.0, 10.0) == 7.5
    assert water_flow.water_column_height(25.0,  0.0) == 25.0
    assert water_flow.water_column_height(48.3, 12.8) == 57.9
    
def test_pressure_gain_from_water_hight():
    assert water_flow.pressure_gain_from_water_height( 0.0) == pytest.approx(0.000  , 0.001)
    assert water_flow.pressure_gain_from_water_height(30.2) == pytest.approx(295.628, 0.001)
    assert water_flow.pressure_gain_from_water_height(50.0) == pytest.approx(489.450, 0.001)

def test_pressure_loss():
    assert water_flow.pressure_loss_from_pipe(0.048692,	0.00,	0.018,	1.75) == pytest.approx(0.000   , 0.001)
    assert water_flow.pressure_loss_from_pipe(0.048692,	200.00,	0.018,	1.75) == pytest.approx(-113.008, 0.001)
    
pytest.main(["-v", "--tb=line", "-rN", __file__])