from enum import Enum

SESSION_KEY = "_lti_tool_launch_id"

CONTEXT_ROLE_PATTERN = "http://purl.imsglobal.org/vocab/lis/v2/membership#{}"

CONTEXT_TYPE_PATTERN = "http://purl.imsglobal.org/vocab/lis/v2/course#{}"


class ContextRole(str, Enum):
    ADMINISTRATOR = CONTEXT_ROLE_PATTERN.format("Administrator")
    CONTENT_DEVELOPER = CONTEXT_ROLE_PATTERN.format("ContentDeveloper")
    INSTRUCTOR = CONTEXT_ROLE_PATTERN.format("Instructor")
    LEARNER = CONTEXT_ROLE_PATTERN.format("Learner")
    MENTOR = CONTEXT_ROLE_PATTERN.format("Mentor")

    @property
    def short_name(self) -> str:
        """Return the short name of this role."""
        return self.value[len(CONTEXT_ROLE_PATTERN.format("")) :]

    @property
    def full_name(self) -> str:
        """Return the full name of this role."""
        return self.value


class ContextType(str, Enum):
    COURSE_TEMPLATE = CONTEXT_TYPE_PATTERN.format("CourseTemplate")
    COURSE_OFFERING = CONTEXT_TYPE_PATTERN.format("CourseOffering")
    COURSE_SECTION = CONTEXT_TYPE_PATTERN.format("CourseSection")
    GROUP = CONTEXT_TYPE_PATTERN.format("Group")

    @property
    def short_name(self) -> str:
        """Return the short name of this context."""
        return self.value[len(CONTEXT_TYPE_PATTERN.format("")) :]

    @property
    def full_name(self) -> str:
        """Return the full name of this context."""
        return self.value
