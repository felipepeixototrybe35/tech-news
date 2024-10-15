from tech_news.analyzer.reading_plan import ReadingPlanService  # noqa: F401, E261, E501
import pytest
from unittest.mock import patch


def test_reading_plan_group_news(mock_find_news):
    # Mockando o retorno da função find_news
    mock_find_news = [
        {"title": "Notícia A", "reading_time": 4},
        {"title": "Notícia B", "reading_time": 3},
        {"title": "Notícia C", "reading_time": 10},
        {"title": "Notícia D", "reading_time": 15},
        {"title": "Notícia E", "reading_time": 12},
    ]

    expected_output = {
        "readable": [
            {
                "unfilled_time": 3,
                "chosen_news": [
                    ("Notícia A", 4),
                    ("Notícia B", 3),
                ],
            },
            {
                "unfilled_time": 0,
                "chosen_news": [
                    ("Notícia C", 10),
                ],
            },
        ],
        "unreadable": [
            ("Notícia D", 15),
            ("Notícia E", 12),
        ],
    }

    with pytest.raises(
        ValueError, match="Valor 'available_time' deve ser maior que zero"
    ):
        ReadingPlanService.group_news_for_available_time(-1)
    with patch(
        'tech_news.analyzer.reading_plan.find_news',
        return_value=mock_find_news
    ):
        # Chamando o método que estamos testando
        result = ReadingPlanService.group_news_for_available_time(10)

        # Verificando se o resultado está correto
        assert result == expected_output
