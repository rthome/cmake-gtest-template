#include "gmock/gmock.h"

#include "example.h"

using namespace testing;

namespace foobar::tests
{
	TEST(ExampleTests, Example) {
		foobar::Example example{};
        ASSERT_THAT(example.getValue(), Eq(99));
	}
}
