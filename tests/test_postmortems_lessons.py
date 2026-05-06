from app.postmortems.lessons import LessonExtractor


def test_lesson_extractor():
    extractor = LessonExtractor()
    assert len(extractor.extract({})) == 0
