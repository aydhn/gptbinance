def activation_guard(verdict):
    if verdict.verdict_class.name != "ALLOW":
        raise Exception("Activation blocked")
