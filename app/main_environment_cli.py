import argparse
from app.environment_plane import (
    CanonicalEnvironmentRegistry, EnvironmentStorage, EnvironmentRepository,
    create_environment_object, EnvironmentClass, generate_environment_summary,
    define_topology, TopologyClass
)

def setup_mock_data(repo: EnvironmentRepository):
    env1 = create_environment_object("staging-1", EnvironmentClass.STAGING, "team-a", "Staging environment 1")
    env1.topology = define_topology(TopologyClass.SHARED, "Shared staging topology")
    repo.save_environment(env1)

def main():
    parser = argparse.ArgumentParser(description="Environment Plane CLI")
    parser.add_argument("--show-environment-registry", action="store_true")
    parser.add_argument("--show-environment", action="store_true")
    parser.add_argument("--environment-id", type=str)

    args = parser.parse_args()

    storage = EnvironmentStorage()
    repo = EnvironmentRepository(storage)
    setup_mock_data(repo)

    if args.show_environment_registry:
        print("Environment Registry:")
        for env in repo.list_environments():
            print(f"- {env.environment_id} ({env.record.environment_class.name})")

    elif args.show_environment:
        if not args.environment_id:
            print("Error: --environment-id is required")
            return
        try:
            env = repo.get_environment(args.environment_id)
            print(generate_environment_summary(env))
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
