from github_scaffolding_generator.validator import validate_all, ValidationError

def test_validate_all_valid():
    context = validate_all(
        project_name="test-project",
        project_type="cli",
        stack="Python 3.12 + Poetry",
        license_name="MIT",
        visibility="public",
        ci_targets="lint,test"
    )
    assert context["project_name"] == "test-project"
    assert context["project_type"] == "cli"
    assert context["license"] == "MIT"

def test_validate_invalid_project_type():
    try:
        validate_all(
            project_name="test",
            project_type="invalid",
            stack="Python 3.12 + Poetry"
        )
        assert False, "Should have raised ValidationError"
    except ValidationError:
        pass

def test_generator():
    from github_scaffolding_generator.generator import Generator
    import tempfile
    import os
    
    with tempfile.TemporaryDirectory() as tmpdir:
        gen = Generator(output_dir=tmpdir)
        context = {
            "project_name": "test-project",
            "project_type": "cli",
            "stack": "Python 3.12 + Poetry",
            "license": "MIT",
            "visibility": "public",
            "ci_targets": ["lint", "test"],
            "description": "Test project",
            "author": "testuser",
            "quick": False
        }
        files = gen.generate(context)
        assert len(files) > 0
        assert any("README.md" in f for f in files)
