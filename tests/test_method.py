import pytest
from src.app import add, subtract, multiply, divide, calculate_power, get_stackoverflow_questions, my_url
from unittest.mock import patch, MagicMock

# Test math operations
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(1, 1) == 0
    assert subtract(-1, -1) == 0
    assert subtract(0, 5) == -5

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 1) == -1
    assert multiply(-1, -1) == 1
    assert multiply(0, 5) == 0

def test_divide():
    assert divide(6, 3) == 2
    assert divide(5, 2) == 2.5
    assert divide(-6, 2) == -3
    assert divide(0, 5) == 0

def test_divide_by_zero():
    with pytest.raises(ValueError) as excinfo:
        divide(5, 0)
    assert "Cannot divide by zero" in str(excinfo.value)

def test_calculate_power():
    assert calculate_power(2, 3) == 8
    assert calculate_power(5, 0) == 1
    assert calculate_power(0, 5) == 0
    assert calculate_power(2, -1) == 0.5

# Test API functions with mocking
@patch('src.app.requests.get')
def test_get_stackoverflow_questions(mock_get):
    # Create a mock response
    mock_response = MagicMock()
    mock_response.json.return_value = {'items': ['question1', 'question2']}
    mock_get.return_value = mock_response
    
     # Call the function
    result = get_stackoverflow_questions()
    
    # Assert the result
    assert result == ['question1', 'question2']
    mock_get.assert_called_once_with('https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow')


@patch('src.app.requests.get')
def test_my_url(mock_get):
    # Create a mock response
    mock_response = MagicMock()
    mock_get.return_value = mock_response
    
#     # Call the function
    result = my_url()
    
#     # Assert the result
    assert result == mock_response
    mock_get.assert_called_once_with('https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow')