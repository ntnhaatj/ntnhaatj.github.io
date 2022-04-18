from abc import ABC, abstractmethod
import argparse
import subprocess
import os
from datetime import datetime


class GenFilePipelineFactory(ABC):
    FILE_PATH = None

    @abstractmethod
    def get_filename(self):
        return "unknown"

    @abstractmethod
    def get_content(self):
        return "unknown"

    @classmethod
    def create_file(cls, filename: str, content: str = "", overwrite: bool = False):
        if not os.path.exists(filename) or overwrite:
            with open(filename, "w") as f:
                f.write(content)
        else:
            raise Exception(f"{filename} existed, "
                            f"enable --overwrite flag to overwrite existed file")

    def post_run(self):
        pass

    def run(self):
        filename = self.get_filename()
        content = self.get_content()

        if not self.FILE_PATH:
            raise NotImplemented("undefined FILE_PATH")

        GenFilePipelineFactory.create_file(
            "/".join((self.FILE_PATH, filename, )),
            content,
            getattr(self, "overwrite", False)
        )


class GenPostPipeline(GenFilePipelineFactory):
    FILE_PATH = "_posts"

    def __init__(self, args: object) -> None:
        self.title = args.title
        self.published_date = datetime.now().strftime("%Y-%m-%d")
        self.tags = args.tags
        self.category = args.category
        self.author = subprocess.run(
            ['git', 'config', 'user.name'], capture_output=True, text=True).stdout.strip('\n')
        self.overwrite = args.overwrite

    def get_filename(self):
        return f"{self.published_date}-{self.title}.md".replace(" ", "-").lower()

    def get_content(self):
        return f"""
---
layout: post
title:  "{self.title}"
date:   {self.published_date}
categories: {self.category}
author: {self.author}
tags: {" ".join(self.tags)}
---
        """.strip()


class GenTagPipeline(GenFilePipelineFactory):
    FILE_PATH = "tag"

    def __init__(self, args: object) -> None:
        self.name = args.name
        self.overwrite = args.overwrite

    def get_filename(self):
        return f"{self.name}.md".replace(" ", "-")

    def get_content(self):
        return f"""
---
layout: tagpage
title: "Tag: {self.name}"
tag: {self.name}
robots: noindex
---
        """.strip()


def gen_new_post(args):
    pipeline = GenPostPipeline(args)
    pipeline.run()


def gen_new_tag(args):
    pipeline = GenTagPipeline(args)
    pipeline.run()


def setup_args():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()
    subparsers.required = True

    # setup new post command parser
    new_post_cmd_parser = subparsers.add_parser(
        "post", description="to generate new post with defined template",
    )
    new_post_cmd_parser.set_defaults(func=gen_new_post)
    new_post_cmd_parser.add_argument(
        "--title", help="post title", required=True
    )
    new_post_cmd_parser.add_argument(
        "--tags", help="post tags", nargs="+", default=tuple()
    )
    new_post_cmd_parser.add_argument(
        "--category", help="post category", default="unknown"
    )
    new_post_cmd_parser.add_argument(
        "--overwrite", help="replace existed post", action=argparse.BooleanOptionalAction
    )

    # setup new tag command parser
    new_tag_cmd_parser = subparsers.add_parser(
        "tag", description="to generate new tag with defined template",
    )
    new_tag_cmd_parser.set_defaults(func=gen_new_tag)
    new_tag_cmd_parser.add_argument(
        "--name", help="tag name", required=True
    )
    new_tag_cmd_parser.add_argument(
        "--overwrite", help="replace existed tag", action=argparse.BooleanOptionalAction
    )
    return parser.parse_args()


def main():
    # run with args
    args = setup_args()
    args.func(args)


if __name__ == "__main__":
    main()
